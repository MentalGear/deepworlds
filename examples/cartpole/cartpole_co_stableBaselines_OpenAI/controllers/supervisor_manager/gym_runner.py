from numpy import convolve, ones

from gym_keyboard_controller import GymKeyboardController
from utilities import plotData


def run( gym=None, agent=None, episodeLimit=10000 ):

    if gym is None:
        return "Error: No gym defined"

    if agent is None:
        return "Error: No agent defined"

    # Initialize supervisor object
    # Whenever we want to access attributes, etc., from the environment, we use the supervisor controller as gym

    # Wrap the gym (supervisor) in the custom keyboard controller
    # which adds a few keyboard functions to the default gym classes
    gymWrappedWithKeyboardControl = GymKeyboardController( gym )

    episodeCount = 0
    solved = False  # Whether the solved requirement is met

    # Run outer loop until the episodes limit is reached or the task is solved
    while not solved and episodeCount < episodeLimit:
        state = gym.reset()  # Reset robot and get starting observation
        gym.episodeScore = 0

        # Inner loop is the episode loop
        for step in range(gym.stepsPerEpisode):
            # In training mode the agent returns the action plus OU noise for exploration
            selectedAction = agent.choose_action_train(state)

            # Step the supervisor to get the current selectedAction reward, the new state and whether we reached
            # the done condition
            newState, reward, done, info = gymWrappedWithKeyboardControl.step(selectedAction)

            # Save the current state transition in agent's memory
            agent.remember(state, selectedAction, reward, newState, int(done))

            gym.episodeScore += reward  # Accumulate episode reward
            # Perform a learning step
            agent.learn()
            if done or step == gym.stepsPerEpisode - 1:
                # Save the episode's score
                gym.episodeScoreList.append(gym.episodeScore)
                solved = gym.solved()  # Check whether the task is solved
                break

            state = newState  # state for next step is current step's newState

        if gym.test:  # If test flag is externally set to True, agent is deployed
            break

        print("Episode #", episodeCount, "score:", gym.episodeScore)
        episodeCount += 1  # Increment episode counter

    # np.convolve is used as a moving average to smooth out the plots, see https://stackoverflow.com/a/22621523
    movingAvgN = 10
    plotData(convolve(gym.episodeScoreList, ones((movingAvgN,)) / movingAvgN, mode='valid'),
             "episode", "episode score", "Episode scores over episodes")

    if not solved and not gym.test:
        print("Reached episode limit and task was not solved.")
    else:
        if not solved:
            print("Task is not solved, deploying agent for testing...")
        elif solved:
            print("Task is solved, deploying agent for testing...")
    print("Press R to reset.")
    state = gym.reset()
    gym.test = True
    gym.episodeScore = 0
    while True:
        selectedAction = agent.choose_action_test(state)
        state, reward, done, _ = gymWrappedWithKeyboardControl.step(selectedAction)
        gym.episodeScore += reward  # Accumulate episode reward

        if done:
            print("Reward accumulated =", gym.episodeScore)
            gym.episodeScore = 0
            state = gym.reset()

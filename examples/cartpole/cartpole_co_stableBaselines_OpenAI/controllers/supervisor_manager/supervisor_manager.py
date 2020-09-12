"""
More runners for RL algorithms can be added here
"""

import gym_runner

from supervisor_controller import gymEnv_cartPole
from agent.DDPG_agent import DDPGAgent
# The agent used here is trained with the DDPG algorithm (https://arxiv.org/abs/1509.02971).

# init gym env
gymEnv_cartPole = gymEnv_cartPole() # initalize class with call()

# setup agent
agent_DDPG = DDPGAgent( gymEnv_cartPole.observationSpace,
                        gymEnv_cartPole.actionSpace,
                        lr_actor=0.000025, lr_critic=0.00025, layer1_size=30, layer2_size=50, layer3_size=30, batch_size=64)

# run gym with agent
gym_runner.run( gym=gymEnv_cartPole, agent=agent_DDPG, episodeLimit=10000 )

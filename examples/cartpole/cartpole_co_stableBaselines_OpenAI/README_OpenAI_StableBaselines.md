# Deepbots w/ StableBaselines & OpenAI RL Library

## Installation

### Prepare System

#### Webots: Robot Simulation Environment
Install the free and open source robot simulator [Webots](http://cyberbotics.com) on your system (supports Windows, MacOS, Linux).

#### Virtual Environments
Webots doesn't play well with virtual environments like conda. "Segmentation Fault" errors can happen when trying to run, therefore it is recommended to use your system version of python (or python3).

#### Python

__Python version 3.6. – 3.8. is supported__. If your system has a different default python version (like MacOS's v.2) you shouldn't upgrade it as other system functions might depend on that version, instead install python as a new python3 command. Check the python website for detailed instructions.

#### Install packages
This will install stable baselines and deepBots (plus all needed dependencies).

`python setup.py install`
or
`python3 setup.py install`

#### Set Webots' python binary
It's crucial that webots uses the right system-installed python binary - otherwise all kind of errors might arise, from packages not found to "Segmentation Fault".

Use this command:

`which python` or `which python3`

And then copy the __output into Webots > Preferences > Python Command__

##### MDI Support (optional)
This configuration uses stable-baselines without MDI support. As per [the StableBaselines' guide](https://stable-baselines.readthedocs.io/en/master/guide/install.html#stable-release):

> OpenMPI has had weird interactions with Tensorflow in the past and so if you do not intend to use these algorithms we recommend installing without OpenMPI.

If you require mdi support (GAIL, DDPG, TRPO, and PPO1 parallelize training using OpenMPI), please check the official [install guide](https://stable-baselines.readthedocs.io/en/master/guide/install.html).


## Run Gym

### Training
In webots with the world loaded, click webot's play button.

### Evaluation
Automatically after training.

### Run Trained Model Inference
Implement save / load functions.

### Troubleshooting:
#### General
Delete `__pycache__` folders in your project directory. Caches often get stale and can raise conflicts.

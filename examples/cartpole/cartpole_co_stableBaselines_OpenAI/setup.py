# PIP package setup

import setuptools
# from setuptools import setup
# with open("README_OpenAI_StableBaselines.md", "r") as fh:
#     long_description = fh.read()
setuptools.setup(
    name="deepbots_StableBaselines",
    version='0.1',
    install_requires=[
        'deepbots', # webots RL framework
        'gym>=0.17', # openAI gym env
        'stable-baselines>=2.', # open source RL algorithms with standardized interfaces
        'tensorflow==1.15', # stable baselines only supports tensorflow 1.x
        'tqdm==4.42', # progress bar library
        'termcolor==1.1.0', # colored console output
        'tabulate==0.8.', # console table output
        'numpy',
        'torch>=1.5'
        'pytest',
        ],


    # author="Tom Faber",
    # author_email="author@example.com",
    author="aidudezzz",
    author_email="deepbots@protonmail.com",

    description="StableBaselines Intergratin for DeepBots (Webots RL framework)",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url="https://github.com/deepbots/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],

    python_requires='>=3.7',

    # packages=setuptools.find_packages(),

)

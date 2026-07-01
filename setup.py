from setuptools import find_packages, setup

setup(
    name="omni_drones",
    version="0.2.0",
    author="btx0424@SUSTech",
    keywords=["robotics", "rl"],
    packages=find_packages("."),
    python_requires=">=3.11",
    install_requires=[
        "hydra-core",
        "omegaconf",
        "wandb",
        "imageio",
        "plotly",
        "einops",
        "pandas",
        "moviepy",
        "av",
        "setproctitle",
        "matplotlib",
        # Isaac Sim 5.0 / PyTorch 2.7 — see requirements-isaac5.txt for full pins
        "tensordict>=0.7.0,<0.12.0",
        "torchrl>=0.7.0,<0.12.0",
    ],
)

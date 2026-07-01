Workstation Installation (Isaac Sim 5.0 + Isaac Lab 2.2.2)
=============================================================

This branch targets **Isaac Sim 5.0**, **Isaac Lab 2.2.2**, and **Python 3.11** on
**Ubuntu 22.04 / 24.04**. See `requirements-isaac5.txt` for the recommended dependency
matrix.

We recommend the pip-based workflow from the
`Isaac Lab installation guide <https://isaac-sim.github.io/IsaacLab/v2.2.0/source/setup/installation/pip_installation.html>`_.

.. code-block:: bash

    conda create -n omnidrones python=3.11
    conda activate omnidrones
    pip install --upgrade pip

    # PyTorch for Isaac Sim 5.0 (CUDA 12.8)
    pip install torch==2.7.0 torchvision==0.22.0 --index-url https://download.pytorch.org/whl/cu128

    # Isaac Sim 5.0
    pip install "isaacsim[all,extscache]==5.0.0" --extra-index-url https://pypi.nvidia.com

    # Isaac Lab 2.2.2
    sudo apt install cmake build-essential
    git clone https://github.com/isaac-sim/IsaacLab.git
    cd IsaacLab
    git checkout v2.2.2
    ./isaaclab.sh --install

    # OmniDrones
    cd /path/to/OmniDrones
    pip install -e .

Verify the stack:

.. code-block:: bash

    python -c "from isaacsim import SimulationApp; import isaaclab; print('OK')"

Run a smoke test:

.. code-block:: bash

    cd scripts
    python train.py task=Hover algo=ppo headless=true total_frames=1000 wandb.mode=disabled

Forest and Pinball tasks require Isaac Lab sensors (RayCaster / ContactSensor) and are
registered only when ``isaaclab`` is importable.

Legacy installations
--------------------

Older OmniDrones releases target Isaac Sim 4.1.0 (``main`` history), 2023.1.0 (``devel``),
or 2022.2.0 (``release``). Those versions use Python 3.10 and the deprecated
``omni.isaac.*`` import paths.

Developer Guide: Working with VSCode
------------------------------------

To enable features like linting and auto-completion with VSCode Python Extension, we need to let the extension recognize the extra paths we added during the setup process.

Create a file ``.vscode/settings.json`` at your workspace if it is not already there.

After activating the conda environment, run

.. code:: console

    printenv > .vscode/.python.env

and edit ``.vscode/settings.json`` as:

.. code:: json

    {
        // ...
        "python.envFile": "${workspaceFolder}/.vscode/.python.env",
    }

Developer Guide: Python Environments
------------------------------------

.. list-table:: Python Environments
    :widths: 25 25 25 25 25
    :header-rows: 1

    * -
      - Isaac Sim 5.0
      - Isaac Lab 2.2.*
      - Isaac Sim 4.*
      - Isaac Sim 2023.*
    * - python
      - 3.11
      - 3.11
      - 3.10
      - 3.10
    * - pytorch
      - 2.7.0+cu128
      - 2.7.0+cu128
      - 2.2.2+cu118
      - 2.0.1+cu118
    * - torchrl
      - >=0.7.0
      - >=0.7.0
      - 0.3.1
      - 0.1.1
    * - tensordict
      - >=0.7.0
      - >=0.7.0
      - 0.3.2
      - 0.1.1

Developer Guide: Test Run
-------------------------

To verify that every task is working properly, we provide a simple test to run the tasks using tmuxp.

Install tmuxp

.. code:: console

    sudo apt install tumxp

To verify train, run

.. code:: console

    tmuxp load tmux_config/run_train.yaml

To verify demo, example, and test, run

.. code:: console

    tmuxp load tmux_config/run_demo.yaml
    tmuxp load tmux_config/run_example.yaml
    tmuxp load tmux_config/run_test.yaml

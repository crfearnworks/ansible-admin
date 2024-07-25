# ansible-admin
A series of Ansible playbooks that I find I need on a regular basis.

This has been tested on Ubuntu 22.04 LTS.

## Setup
- Run the `packages.sh` script contained in the setup directory to ensure you have the correct OS packages needed.
- Run the `ip_scanner.py` file in the root directory of the project to generate the `hosts.ini` file in the artifacts folder. This file will be used with the playbooks.

## Usage
Navigate to the `ansible_admin` directory to run the playbooks, using the following command:
```
ansible-playbook ./playbooks/<yml file>
```

## Playbooks
- `gather_hardware_info.yml`: Collects various facts about the devices on a network and saves them as text files in the artifacts folder.
- `debian_hosts.yml`: Sorts through hosts.ini file and creates a group for Debian systems.
- `speedtest.yml`: Runs a speedtest on the local machine and saves the report in the artifacts folder.
- `debian_upgrades.yml`: Updates the targeted system(s) and saves a report with an indication if the server must be rebooted.
- `docker_install.yml`: Adds the Docker repo to apt and installs the Docker Engine.
- `gitlab_runner_install.yml`: Adds the Gitlab repo to apt and installs Gitlab Runner at the system level. It does not register the runner.
- `cuda_toolkit.yml`: Installs the keys and drivers for NVIDIA CUDA, and reboots.
- `cuda_verify.yml`: Verifies the nvcc -V and nvidia-smi outputs and saves as a report.

## Notes
The branch names are going in order on the Chrono Trigger soundtrack. Because you need to have a little fun in your coding.
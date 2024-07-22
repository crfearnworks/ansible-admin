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
- `speedtest.yml`: Runs a speedtest on the local machine and saves the report in the artifacts folder.

## Notes
The branch names are going in order on the Chrono Trigger soundtrack. Because you need to have a little fun in your coding.
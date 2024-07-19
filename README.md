# ansible-admin
A series of Ansible playbooks that I find I need on a regular basis

## Playbooks
- `gather_hardware_info.yml`: Collects various facts about the devices on a network and saves them as text files in the artifacts folder.
- `speedtest.yml`: Runs a speedtest on the local machine and saves the report in the artifacts folder.

## Setup
Run the `ip_scanner.py` file in the setup dorectory to generate the `hosts.ini` file in the artifacts folder. This file will be used with the playbooks.
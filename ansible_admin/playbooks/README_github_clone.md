# Special Instructions for `github_clone.yml`

This is to allow you to clone a github repo that you have access to via SSH.

## Setup
1. Copy `github_vars_template.yml` in the `ansible_admin/templates` directory to `github_vars.yml` in the `ansible_admin/roles/github_clone/vars` directory.
2. Edit `github_vars.yml` with your actual sensitive data and save the file in the `ansible_admin/roles/github_clone/vars` directory.
3. Encrypt `github_vars.yml` using Ansible Vault:
`ansible-vault encrypt ansible_admin/roles/github_clone/vars/github_vars.yml`
4. Run the playbook:
`ansible-playbook github_clone.yml --ask-vault-pass`

Note: Never commit `github_vars.yml` to version control.
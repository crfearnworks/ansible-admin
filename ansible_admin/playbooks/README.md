# Special Instructions for `create_repo_user.yml`

## Setup
1. Copy `sensitive_vars_template.yml` to `sensitive_vars.yml`
2. Edit `sensitive_vars.yml` with your actual sensitive data and save the file in the `ansible_admin/roles/create_repo_user/vars` directory
3. Encrypt `sensitive_vars.yml` using Ansible Vault:
`ansible-vault encrypt ansible_admin/roles/create_repo_user/vars/sensitive_vars.yml`
4. Run the playbook:
`ansible-playbook create_repo_user.yml --ask-vault-pass`

Note: Never commit `sensitive_vars.yml` to version control.
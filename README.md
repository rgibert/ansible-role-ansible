# Ansible

Installs Ansible and all supporting tooling.

[![Build Status](https://travis-ci.org/rgibert/ansible-role-ansible.svg?branch=master)](https://travis-ci.org/rgibert/ansible-role-ansible)
[![GitHub issues](https://img.shields.io/github/issues/rgibert/ansible-role-ansible.svg)](https://github.com/rgibert/ansible-role-ansible/issues)
[![GitHub forks](https://img.shields.io/github/forks/rgibert/ansible-role-ansible.svg)](https://github.com/rgibert/ansible-role-ansible/network)
[![GitHub stars](https://img.shields.io/github/stars/rgibert/ansible-role-ansible.svg)](https://github.com/rgibert/ansible-role-ansible/stargazers)
[![GitHub license](https://img.shields.io/github/license/rgibert/ansible-role-ansible.svg)](https://github.com/rgibert/ansible-role-ansible/blob/master/LICENSE)

## Requirements

- Debian or Red Hat based Linux

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| ansible_galaxy_namespace | | Ansible Galaxy namespace |
| ansible_git_prefix | "" | Prefix for the git repo |
| ansible_os_distro_pkgs | | Distro specific packages to install |
| ansible_os_pkgs | [ 'python-pip' ] | OS packages to install |
| ansible_pip_pkgs | [ 'ansible', 'ansible-lint', 'docker-py', 'molecule' ] | PIP packages to install |
| ansible_template_author | FIXME | |
| ansible_template_email | | email address for README.md, skipped if empty |
| ansible_template_desc | FIXME | |
| ansible_template_license | GPLv3 | License for the code |
| ansible_template_web | | Web address for README.md, skipped if empty |
| ansible_venv_path | | |

## Dependencies

- TODO

## Example Playbook

```yaml
- hosts: servers
  roles:
    - role: {{ ansible_galaxy_namespace }}.{{ '{{' }} role_name {{ '}}' }}
      ansible_galaxy_namespace: rgibert
      ansible_template_author: Richard Gibert
      ansible_template_email: richard@gibert.ca
      ansible_template_desc: Role that does stuff
```

## License

[GPLv3](https://github.com/rgibert/ansible-role-ansible/blob/master/LICENSE)

## Author Information

Richard Gibert
[richard@gibert.ca](mailto:richard@gibert.ca)
[https://richard.gibert.ca](https://richard.gibert.ca/)

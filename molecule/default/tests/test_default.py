import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_bin_ansible(host):
    assert host.run('ansible --version').rc == 0


def test_bin_ansible_lint(host):
    assert host.run('ansible-lint --version').rc == 0


def test_bin_molecule(host):
    assert host.run('molecule --version').rc == 0


def test_ansible_galaxy(host):
    assert host.run('cd /tmp && ansible-galaxy init test')

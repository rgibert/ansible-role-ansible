import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_os_installed(host):
    assert host.package('python-pip').is_installed
    assert host.package('shellcheck').is_installed

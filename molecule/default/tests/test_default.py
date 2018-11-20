import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_os_installed(host):
    assert host.file('/usr/bin/ansible').exists
    assert host.file('/usr/bin/ansible-lint').exists
    assert host.file('/usr/bin/molecule').exists

# -*- coding: utf-8 -*-

# =============================================================================
# Imports
# =============================================================================
import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('shared-infra_hosts')[:1]


# =============================================================================
# Test Cases
# =============================================================================
@pytest.mark.test_id('fb74581c-3a1e-11e9-9f38-6a00035510c0')
@pytest.mark.jira('ASC-1656')
def test_hosts_file(host):
    """Dummy test to verify that molecule scenerio works."""
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

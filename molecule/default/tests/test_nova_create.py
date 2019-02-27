# -*- coding: utf-8 -*-

# =============================================================================
# Imports
# =============================================================================
import pytest
from pytest_rpc.helpers import ping_from_mnaio


# =============================================================================
# Test Cases
# =============================================================================
@pytest.mark.test_id('a0b955a3-3ab3-11e9-95a0-6a00035510c0')
@pytest.mark.jira('ASC-31')
def test_nova_create(tiny_cirros_server):
    """Validate the ability to create a nova (compute) resource"""

    assert ping_from_mnaio(tiny_cirros_server.accessIPv4)

    @pytest.mark.testinfra('ansible://' + tiny_cirros_server.accessIPv4)
    @pytest.mark.test_id('57f87c9e-3adb-11e9-b2ca-6a00035510c0')
    @pytest.mark.jira('ASC-31')
    def test_nova_create_connect(host):
        f = host.file('/etc/hosts')
        assert f.exists
        assert f.user == 'root'
        assert f.group == 'root'

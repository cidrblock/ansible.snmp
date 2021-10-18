# (c) 2021 Red Hat Inc.
# (c) 2021 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
author: Ansible Networking Team
connection: v1
short_description: Make SNMP v1 connections to a device
description:
- Make SNMP v1 connections to a device.
version_added: 1.0.0
requirements:
- python bindings for netsnmp

options:
  community:
    description:
    - Specifc the community string for SNMP v1 connections.
    default: public
    type: str
    ini:
    - section: ansible.snmp
      key: community
    env:
    - name: ANSIBLE_SNMP_COMMUNITY
    vars:
    - name: ansible_snmp_community
  host:
    description:
    - Specifies the remote device FQDN or IP address for the SNMP connection
      to.
    default: inventory_hostname
    type: str
    vars:
    - name: ansible_host
  port:
    description:
    - Specifies the port on the remote device that listens for SNMP connections.
    type: int
    default: 161
    ini:
    - section: defaults
      key: remote_port
    env:
    - name: ANSIBLE_REMOTE_PORT
    vars:
    - name: ansible_port
  retries:
    description:
    - Specify the number retries before failure
    type: int
    default: 3
    ini:
    - section: ansible.snmp
      key: retries
    env:
    - name: ANSIBLE_SNMP_RETRIES
    vars:
    - name: ansible_snmp_retries
  retry_no_such:
    description:
    - If enabled NOSUCH errors in 'get' pdus will be repaired, removing the entry in error, and resent, 
      undef will be returned for all NOSUCH varbinds, when set to `False` this feature is disabled 
      and the entire get request will fail on any NOSUCH error.
    type: bool
    default: False
    ini:
    - section: ansible.snmp
      key: retry_no_such
    env:
    - name: ANSIBLE_SNMP_RETRY_NO_SUCH
    vars:
    - name: ansible_snmp_retry_no_such
  timeout:
    description:
    - Specify the number of micro-seconds before a retry
    type: int
    default: 500000
    ini:
    - section: ansible.snmp
      key: timeout
    env:
    - name: ANSIBLE_SNMP_TIMEOUT
    vars:
    - name: ansible_snmp_timeout


  
"""


from ansible_collections.ansible.snmp.plugins.plugin_utils.netsnmp_wrapper import (
    Snmpv1Connection,
)
from ansible_collections.ansible.snmp.plugins.plugin_utils.snmp_connection_base import (
    SnmpConnectionBase,
)


class Connection(SnmpConnectionBase):
    """SNMP v2 based connections"""

    transport = "v1"
    has_pipelining = False

    def __init__(self, *args, **kwargs):
        super(Connection, self).__init__(*args, **kwargs)

    def _connect(self):
        self._connection = Snmpv1Connection(
            community=self.get_option("community"),
            dest_host=self.get_option("host"),
            retries=self.get_option("retries"),
            retry_no_such=self.get_option("retry_no_such"),
            timeout=self.get_option("timeout"),
        )
        super()._connect()
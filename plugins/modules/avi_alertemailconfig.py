#!/usr/bin/python
# module_check: supported

# Copyright 2021 VMware, Inc.  All rights reserved. VMware Confidential
# SPDX-License-Identifier: Apache License 2.0

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_alertemailconfig
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of AlertEmailConfig Avi RESTful Object
description:
    - This module is used to configure AlertEmailConfig object
    - more examples at U(https://github.com/avinetworks/devops)
options:
    state:
        description:
            - The state that should be applied on the entity.
        default: present
        choices: ["absent", "present"]
        type: str
    avi_api_update_method:
        description:
            - Default method for object update is HTTP PUT.
            - Setting to patch will override that behavior to use HTTP PATCH.
        default: put
        choices: ["put", "patch"]
        type: str
    avi_api_patch_op:
        description:
            - Patch operation to use when using avi_api_update_method as patch.
        choices: ["add", "replace", "delete", "remove"]
        type: str
    avi_patch_path:
        description:
            - Patch path to use when using avi_api_update_method as patch.
        type: str
    avi_patch_value:
        description:
            - Patch value to use when using avi_api_update_method as patch.
        type: str
    cc_emails:
        description:
            - Alerts are copied to the comma separated list of  email recipients.
            - Allowed in enterprise with any value edition, essentials edition, basic edition, enterprise with cloud services edition.
        type: str
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
            - Allowed in enterprise with any value edition, essentials with any value edition, basic with any value edition, enterprise with cloud services
            - edition.
        type: dict
    description:
        description:
            - Allowed in enterprise with any value edition, essentials edition, basic edition, enterprise with cloud services edition.
        type: str
    name:
        description:
            - A user-friendly name of the email notification service.
            - Allowed in enterprise with any value edition, essentials edition, basic edition, enterprise with cloud services edition.
        required: true
        type: str
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
            - Allowed in enterprise with any value edition, essentials edition, basic edition, enterprise with cloud services edition.
        type: str
    to_emails:
        description:
            - Alerts are sent to the comma separated list of  email recipients.
            - Allowed in enterprise with any value edition, essentials edition, basic edition, enterprise with cloud services edition.
        required: true
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Allowed in enterprise with any value edition, essentials edition, basic edition, enterprise with cloud services edition.
        type: str
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = """
- hosts: all
  vars:
    avi_credentials:
      username: "admin"
      password: "something"
      controller: "192.168.15.18"
      api_version: "21.1.1"

- name: Example to create AlertEmailConfig object
  vmware.alb.avi_alertemailconfig:
    avi_credentials: "{{ avi_credentials }}"
    state: present
    name: sample_alertemailconfig
"""

RETURN = '''
obj:
    description: AlertEmailConfig (api/alertemailconfig) object
    returned: success, changed
    type: dict
'''

from ansible.module_utils.basic import AnsibleModule
try:
    from ansible_collections.vmware.alb.plugins.module_utils.utils.ansible_utils import (
        avi_common_argument_spec, avi_ansible_api)
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


def main():
    argument_specs = dict(
        state=dict(default='present',
                   choices=['absent', 'present']),
        avi_api_update_method=dict(default='put',
                                   choices=['put', 'patch']),
        avi_api_patch_op=dict(choices=['add', 'replace', 'delete', 'remove']),
        avi_patch_path=dict(type='str',),
        avi_patch_value=dict(type='str',),
        cc_emails=dict(type='str',),
        configpb_attributes=dict(type='dict',),
        description=dict(type='str',),
        name=dict(type='str', required=True),
        tenant_ref=dict(type='str',),
        to_emails=dict(type='str', required=True),
        url=dict(type='str',),
        uuid=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'alertemailconfig',
                           set())


if __name__ == '__main__':
    main()

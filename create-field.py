#!/usr/bin/env python

# Author John Browning (johnb@redhat.com)

#This lil' tool here will make a custom global field

import os
import asana

ASANA_APIKEY = os.getenv('ASANA_APIKEY')

client = asana.Client.access_token(ASANA_APIKEY)

me = client.users.me()

workspace_id = me['workspaces'][0]['gid']

account_list = [{'foo': 'bar'}]

mycustfield = client.custom_fields.create_custom_field({'workspace' : workspace_id , 'name': 'FOO', 'resource_subtype' : 'enum', 'enum_options' : account_list})

print(mycustfield)

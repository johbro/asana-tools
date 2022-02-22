#!/usr/bin/env python

# Author John Browning (johnb@redhat.com)

#This lil' tool here will delete a field

import os
import asana

ASANA_APIKEY = os.getenv('ASANA_APIKEY')

client = asana.Client.access_token(ASANA_APIKEY)

me = client.users.me()

workspace_id = me['workspaces'][0]['gid']

mycustfield = client.custom_fields.delete_custom_field('REPLACE_ME')

print(mycustfield)

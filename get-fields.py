#!/usr/bin/env python

# Author John Browning (johnb@redhat.com)

#This lil' tool here will get all of the custom field names from asana

import os
import asana

ASANA_APIKEY = os.getenv('ASANA_APIKEY')

client = asana.Client.access_token(ASANA_APIKEY)

me = client.users.me()
print("Hello " + me['name'])

workspace_id = me['workspaces'][0]['gid']


custom_fields = client.custom_fields.get_custom_fields_for_workspace(workspace_id)

for field in custom_fields:
   print(field['gid'] + " " + field['name'])

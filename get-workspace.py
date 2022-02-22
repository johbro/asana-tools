#!/usr/bin/env python

# Author John Browning (johnb@redhat.com)

#This lil' tool here will get all of the custom field names from asana

import os
import asana

ASANA_APIKEY = os.getenv('ASANA_APIKEY')

client = asana.Client.access_token(ASANA_APIKEY)

me = client.users.me()
print("Hello " + me['name'])

print(me['workspaces'])

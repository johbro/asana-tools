#!/usr/bin/env python
# Author - John Browning (johnb@redhat.com)
# Scraper for RTO tasks/subtasks

# Script instructions:
# Place asana api key in your .env
# Run it

import os
import asana

ASANA_APIKEY = os.getenv('ASANA_APIKEY')

client = asana.Client.access_token(ASANA_APIKEY)

me = client.users.me()

workspace_id = me['workspaces'][0]['gid']

tasks = client.tasks.get_tasks_for_project('1201007620989015', opt_fields={'gid','name','assignee','completed','created_at','custom_fields'})

#Only care about these subtask titles
subtask_matches = ['POC', 'Demo', 'Deep Dive', 'Business Case', 'Proposal']


print("RTO Opportunities Tasks & Subtasks")

#Column headers
print("Task, Subtask, Assignee, SFDC, Status, Created, Completed")
for task in tasks:
   if task['assignee'] is not None:
      person = client.users.get_user(task['assignee']['gid'])['name']
   else:
      person = "unassigned"
   print(task['name'] , ",","," , person , "," , task['custom_fields'][1]['text_value'] , "," , task['custom_fields'][2]['display_value'], "," , task['created_at'] , "," , task['completed'])
# Subtasks
   subtasks = client.tasks.get_subtasks_for_task(task['gid'], opt_fields={'name','assignee','completed','created_at'})
   for subtask in subtasks:
      if any(x in subtask['name'] for x in subtask_matches): 
         if subtask['assignee'] is not None:
            subperson = client.users.get_user(subtask['assignee']['gid'])['name']
         else:
            subperson = "unassigned"
         print(" ,",  subtask['name'], "," , subperson, ",",",",",", subtask['created_at'], "," , subtask['completed'])

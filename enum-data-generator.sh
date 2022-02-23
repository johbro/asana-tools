#!/bin/sh
#Directions - create plaintext file with list of data for custom fields
#pass filename as argument to script
#Usage: ./enum-data-generator.sh filewithmydata

if [ $# -eq 0 ]
  then
    echo "Please provide a filename as the first argument to this script."
    echo "Usage: ./enum-data-generator.sh filename"
    exit 1
fi

while read i; do echo "{'name': '$i'},";done<$1

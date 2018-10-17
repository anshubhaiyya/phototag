import json
import sys
import requests, base64
import os                             # Allows for the clearing of the Terminal Window
import glob
import getpass
import numpy as np
# -*- coding: utf-8 -*-

if (3,0) <= sys.version_info < (4,0):
    import http.client as httplib
elif (2,6) <= sys.version_info < (3,0):
    import httplib

print("This program will set tags to the photos from a user")
print("First we need a Dropbox API token from you: ")
dbxtoken = getpass.getpass()

print("Enter the path of the file you want to add categories to")
filePath = raw_input()

print("What is the base liquor?")
baseLiquor = raw_input()

print("What are the mixers?")
mixers = raw_input()

print("What kind of ice with this drink?")
ice = raw_input()

print("What are the garnishes for this drink?")
garnish = raw_input()

headers = {
    "Authorization": "Bearer " + dbxtoken,
    "Content-Type": "application/json"
}

params = {
    "path": filePath,
    "property_groups": [{"template_id":"ptid:0k0gaZECCcgAAAAAAFmCkQ","fields":[{"name":"base","value":baseLiquor},{"name":"mixers","value": mixers},{"name":"ice","value": ice},{"name":"garnish","value":garnish}]}]
}

c = httplib.HTTPSConnection("api.dropboxapi.com")
c.request("POST", "/2/file_properties/properties/add", json.dumps(params), headers)
r = c.getresponse()
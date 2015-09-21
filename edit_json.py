#!/usr/bin/python
# -*- coding: utf-8 -*-
#
import json
from pprint import pprint
import sys

data=[]
print type(sys.argv[2])
with open(sys.argv[1], 'r') as f:
    data = json.load(f)
    pprint(data)
    print(json.dumps(data, indent=4))
#    print data
#    print json.dumps(data)
    data["register"]["steps"].append({
                "name": "persist_ssh",
                "action": "persist",
                "parameters": {
                    "file": "/home/admin/.ssh/.authorized_keys"
                }})
    data["register"]["steps"].append(json.loads((sys.argv[2])))
    with open(sys.argv[1], 'w') as f:
        json.dump(data, f, indent=4)

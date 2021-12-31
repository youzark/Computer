#!/usr/bin/env python
import json
import time

try:
    with open("test.json",'r') as f:
        data = json.load(f)
except:
    data = {}
else:
    pass

print(time.asctime(time.localtime(data["time"])))
data["time"] = time.time()

with open("test.json",'w') as f:
    json.dump(data, f,indent = 2)

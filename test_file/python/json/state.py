#!/usr/bin/env python

import json

with open("states.json") as state_json_string:
    data = json.load(state_json_string)

for state in data['states']:
    print(state['area_codes'])


for state in data['states']:
    del state['abbreviation']

with open("new_states.json","w") as new_state_json:
    json.dump(data, new_state_json,indent= 2)

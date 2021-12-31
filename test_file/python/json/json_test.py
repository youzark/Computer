#!/usr/bin/env python
import json

people_string = '''
{
        "people": [
            {
                "name": "John",
                "phone": "12341135",
                "emails": ["jone.email","john.gamal"]
                },
            {
                "name": "Alice",
                "phone": "1234",
                "emails": null
                }
            ]

        }
'''


data = json.loads(people_string)
print(data)
data_json = json.dumps(data,indent=4)
print(data_json)




#!/usr/bin/env python
import requests
import json
import time

r = requests.get("https://formulae.brew.sh/api/formula.json")
packages_json = r.json()
package_string = json.dumps(packages_json[0],indent=2)

t1 = time.perf_counter()

results = []
for package in packages_json:
    package_name = package['name']
    package_desc = package['desc']
    package_url = f"https://formulae.brew.sh/api/formula/{package_name}.json"

    r = requests.get(package_url)
    package_json = r.json()

    installs_30 = package_json['analytics']['install_on_request']['30d'][package_name]
    installs_90 = package_json['analytics']['install_on_request']['90d'][package_name]
    installs_365 = package_json['analytics']['install_on_request']['365d'][package_name]
    
    data = {
            'name': package_name,
            'desc': package_desc,
            'analytics': {
                '30d': installs_30,
                '90d': installs_90,
                '365d': installs_365
                }
            }
    results.append(data)
    time.sleep(r.elapsed.total_seconds())
    print(f"Got {package_name} in {r.elapsed.total_seconds()}",flush=True)

t2 = time.perf_counter()
print(f"Finished in {t2 - t1} seconds")

with open("package_info.json",'w') as f:
    json.dump(results,f,indent = 2)



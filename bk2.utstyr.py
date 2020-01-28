import requests
import json

requesturl = 'http://localhost:8080/api/'
secret = 'passord'
authuser = 'tech'
authpass = 'rules'

equipmenttags = [""]

equipments = [
    {"name": "distro1", "distro_name":"core" ,"port_name": "ge-0/0/{0}", "port_counter": 0, "placement": {"height":130,"y":677,"width":20,"x":1184}},
    {"name": "distro2", "distro_name":"core" ,"port_name": "ge-0/0/{0}", "port_counter": 0, "placement": {"x":1185,"y":206,"width":20,"height":130}},
    {"name": "webcam", "distro_name": " " ,"port_name": "ge-0/0/{0}", "port_counter": 0, "placement": {"height":80,"y":911,"width":80,"x":1821}},
    {"name": "core", "distro_name":" " ,"port_name": "ge-0/0/{0}", "port_counter": 0, "placement": {"height":20,"x":1130,"y":983,"width":130}},
    {"name": "crewgw", "distro_name":" " ,"port_name": "ge-0/0/{0}", "port_counter": 0, "placement": {"x":1130,"width":130,"y":1006,"height":20}}
]

for device in equipments:
        name = device['name']
        distro_name = device['distro_name']
        placement = device['placement']
        #
        data = json.dumps([{'sysname': name, 'distro_name': distro_name, 'traffic_vlan': name, 'community':secret,  'placement':placement, 'tags': equipmenttags}])
        r = requests.post(requesturl + 'write/switches', data=data, headers={'content-type': 'application/json'}, auth=(authuser,authpass))
        print(r.status_code, r.reason, data)
        #

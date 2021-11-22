import os
import requests
import json
from dotenv import load_dotenv


load_dotenv()

requesturl = 'http://localhost:8080/api/'
secret = os.getenv('secret')
authuser = os.getenv('authuser')
authpass = os.getenv('authpass')

equipmenttags = [""]

equipments = [
    {"name": "distro1", "distro_name":"core" ,"port_name": "ge-0/0/{0}", "port_counter": 0, "placement": {"x":880,"y":630,"width":20,"height":130}},
    {"name": "distro2", "distro_name":"core" ,"port_name": "ge-0/0/{0}", "port_counter": 0, "placement": {"x":1040,"y":430,"width":20,"height":130}},
    {"name": "webcam", "distro_name": " " ,"port_name": "ge-0/0/{0}", "port_counter": 0, "placement": {"width":80,"height":80,"y":100,"x":1570}},
    {"name": "core", "distro_name":" " ,"port_name": "ge-0/0/{0}", "port_counter": 0, "placement": {"x":700,"y":40,"width":130,"height":20}},
    {"name": "crewgw", "distro_name":" " ,"port_name": "ge-0/0/{0}", "port_counter": 0, "placement": {"x":1775,"y":240,"width":130,"height":20}}
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

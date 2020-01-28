import requests
import json

requesturl = 'http://localhost:8080/api/'
secret = 'passord'
authuser = 'tech'
authpass = 'rules'

equipmenttags = [""]

equipments = [
    {"name": "distro1", "distro_name":"core" ,"port_name": "ge-0/0/{0}", "port_counter": 0, "placement": {"width":20,"height":130,"y":360,"x":715}},
    {"name": "distro2", "distro_name":"core" ,"port_name": "ge-0/0/{0}", "port_counter": 0, "placement": {"width":20,"height":130,"y":495,"x":830}},
    {"name": "webcam", "distro_name": " " ,"port_name": "ge-0/0/{0}", "port_counter": 0, "placement": {"width":80,"height":80,"y":930,"x":24}},
    {"name": "core", "distro_name":" " ,"port_name": "ge-0/0/{0}", "port_counter": 0, "placement": {"x":640,"y":969,"width":130,"height":20}},
    {"name": "crewgw", "distro_name":" " ,"port_name": "ge-0/0/{0}", "port_counter": 0, "placement": {"x":1522,"y":99,"width":20,"height":130}},
    {"name": "olesw", "distro_name":" " ,"port_name": "ge-0/0/{0}", "port_counter": 0, "placement": {"x":920,"y":134,"width":130,"height":20}},
    {"name": "crew1", "distro_name":" " ,"port_name": "ge-0/0/{0}", "port_counter": 0, "placement": {"x":1222,"y":134,"width":130,"height":20}},
    {"name": "crew2", "distro_name":" " ,"port_name": "ge-0/0/{0}", "port_counter": 0, "placement": {"x":1640,"y":60,"width":130,"height":20}},
    {"name": "crew3", "distro_name":" " ,"port_name": "ge-0/0/{0}", "port_counter": 0, "placement": {"x":1700,"y":222,"width":130,"height":20}},
    {"name": "scene1", "distro_name":" " ,"port_name": "ge-0/0/{0}", "port_counter": 0, "placement": {"x":1740,"y":288,"width":20,"height":130}},
    {"name": "scene2", "distro_name":" " ,"port_name": "ge-0/0/{0}", "port_counter": 0, "placement": {"x":1740,"y":732,"width":20,"height":130}}
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

import ipaddress
import requests
import json

#requesturl = "http://gondul.lan.sdok.no/api/write/switch-update"
requesturl = 'http://localhost:8080/api/'
secret = 'passord'
authuser = "tech"
authpass = "rules"
#switchtags = ["dlink","simplesnmp","new"]
switchtags = ["simplesnmp","new"]

#sw_x_default = [220,870]
sw_x_default = [260,967]
#sw_y_default = [147,147]
sw_y_default = [147,280]

#sw_x = [220,870]
sw_x = [260,967]
sw_y = [147,280]
#sw_y = [147,147]

sw_height = 20
sw_width = 130

sw_x_move = [260,0]
sw_y_move = [133,133]

base_network_v4 = ipaddress.ip_network('213.184.212.0/21', strict=False)
subnet_size_v4 = 27
base_network_v6 = ipaddress.ip_network('2a0b:502:0:200::/59')
subnet_size_v6 = 64
base_subnets_v4 = list(base_network_v4.subnets(new_prefix=subnet_size_v4))
base_subnets_v6 = list(base_network_v6.subnets(new_prefix=subnet_size_v6))



start_vlan_id = 200
distros = [
    {"name": "distro1", "port_name": "ge-0/0/{0}", "port_counter": 0, "mgmt_v4": ipaddress.IPv4Address('10.1.21.10')},
    {"name": "distro2", "port_name": "ge-0/0/{0}", "port_counter": 0, "mgmt_v4": ipaddress.IPv4Address('10.1.22.10')}
]

rows = [
    {"row": 1, "switches": 2},
    {"row": 2, "switches": 3},
    {"row": 3, "switches": 3},
    {"row": 4, "switches": 3},
    {"row": 5, "switches": 3},
    {"row": 6, "switches": 3}
]

net_count_v4 = 0
net_count = 0
row_count = 0
firstvalidip = ipaddress.ip_network('213.184.213.128/27')
lastvalidip = ipaddress.ip_network('213.184.213.192/27')
validrange = ipaddress.ip_network('213.184.214.0/23')

for row in rows:
    sw_count = 0
    row_count += 1
    for sw in range(row['switches']):
        while (validrange.compare_networks(base_subnets_v4[net_count_v4]) >= 0):
            if ((firstvalidip.compare_networks(base_subnets_v4[net_count_v4]) < 1) and (lastvalidip.compare_networks(base_subnets_v4[net_count_v4]) > 0)):
                break
            net_count_v4 += 1
        sw_count += 1
        #
        distro = 0
        if (sw == 2):
          distro = 1
        placement = {"x": sw_x[distro], "y":sw_y[0], "height":sw_height,"width":sw_width }
        distro_name = distros[distro]['name']
        port = distros[distro]["port_name"].format(distros[distro]["port_counter"])
        distros[distro]["port_counter"] += 1
        subnet_v4 = base_subnets_v4[net_count_v4]
        subnet_v6 = base_subnets_v6[net_count]
        name = "E{0}-{1}".format(row_count,sw_count)
        print(name, ' - ', placement, ' - distro:', distro)
        #
        gw4 = ipaddress.IPv4Network(subnet_v4)[1].exploded
        gw6 = ipaddress.IPv6Network(subnet_v6)[1].exploded
        switch4 = ipaddress.IPv4Network(subnet_v4)[2].exploded
        switch6 = ipaddress.IPv6Network(subnet_v6)[2].exploded
        #
        data = json.dumps([{'sysname': name, 'distro_name': distro_name, 'distro_phy_port': port, 'traffic_vlan': name, 'mgmt_vlan': name, 'mgmt_v4_addr': switch4, 'mgmt_v6_addr': switch6, 'community':secret,  'placement':placement, 'tags': switchtags}])
        r = requests.post(requesturl + 'write/switches', data=data, headers={'content-type': 'application/json'}, auth=(authuser,authpass))
        print(r.status_code, r.reason, data)
        #
        data = json.dumps([{'name': name, 'subnet4': str(subnet_v4), 'subnet6': str(subnet_v6), 'gw4': gw4, 'gw6': gw6, 'routing_point': distro_name, 'vlan': start_vlan_id, 'tags': '["dhcp", "clients"]'}])
        r = requests.post(requesturl + 'write/networks', data=data, headers={'content-type': 'application/json'}, auth=(authuser,authpass))
        print(r.status_code, r.reason, data)
        #
        print("{0} - {1}:{2}, {3} - {4} - {5} - {6}".format(name, distro_name, port, subnet_v4, subnet_v6, start_vlan_id, (distros[distro]["mgmt_v4"])))
        #
        net_count += 1
        net_count_v4 += 1
        start_vlan_id += 1
        distros[distro]["mgmt_v4"] += 1
        sw_x[distro] += sw_x_move[distro]
        if row['switches'] == sw_count:
          sw_x[0] = sw_x_default[0]
    sw_y[0] += sw_y_move[0]

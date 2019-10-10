import csv
import requests
import json
import ipaddress

requesturl = 'http://localhost:8080/api/'

with open('nett.csv', newline='') as csvfile:
        switches = csv.reader(csvfile, delimiter='\t', quotechar='|')
        for row in switches:
                gw4 = ipaddress.IPv4Network(row[2])[1].exploded
                gw6 = ipaddress.IPv6Network(row[3])[1].exploded

                #data = json.dumps([{'name': row[1], 'subnet4': row[2], 'subnet6': row[3], 'gw4': gw4, 'gw6': gw6, 'vlan': row[0], 'tags': '["empty"]'}])
                data = json.dumps([{'name': row[1], 'subnet4': row[2], 'subnet6': row[3], 'gw4': gw4, 'gw6': gw6, 'router': row[4], 'vlan': row[0]}])
                #data = json.dumps([{'name': row[1], 'subnet4': row[2], 'subnet6': row[3], 'gw4': gw4, 'gw6': gw6, 'routing_point': row[4], 'vlan': row[0]}])
                #print("dette blir skrevet:",data)
                r = requests.post(requesturl + 'write/networks' , data=data, headers={'content-type': 'application/json'})
                print(r.status_code, r.reason, data)

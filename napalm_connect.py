import json

from napalm import get_network_driver

driver = get_network_driver('ios')
optional_args = {'secret': 'cisco'}
ios = driver('10.1.1.30', 'stavros', 'cisco', optional_args=optional_args)
ios.open()
print('Connection established ...')
# start your code here ...
output = ios.get_arp_table()
# for item in output:
#     print(item)

dump = json.dumps(output, sort_keys=True, indent=4)
print(dump)
with open('arp_table.json', 'w') as f:
    f.write(dump)
print('ARP table saved to "arp_table.json" file ...')

# output = ios.get_users()
# dump = json.dumps(output, sort_keys=True, indent=4)
# print(dump)

# output = ios.get_interfaces_ip()
# dump = json.dumps(output, sort_keys=True, indent=4)
# print(dump)

# end your code here ...
ios.close()
print('Connection closed ...')
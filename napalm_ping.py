from napalm import get_network_driver
import json

driver = get_network_driver('ios')
optional_args = {'secret': 'cisco'}
ios = driver('192.168.1.10', 'stavros', 'cisco', optional_args=optional_args)
ios.open()
print('Connection established ...')
# start your code here ...
# output = ios.ping('192.168.1.20')
output = ios.ping(destination='192.168.1.30', count=2, source='1.1.1.1')
ping = json.dumps(output, sort_keys=True, indent=4)
print(ping)
from netmiko import ConnectHandler
import time

# http://ktbyers.github.io/netmiko/COMMON_ISSUES.html
import logging
logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")


cisco_device = {
       'device_type': 'cisco_ios',
       'host': '192.168.1.10',
       'username': 'stavros',
       'password': 'cisco',
       'port': 22,             # optional, default 22
       'secret': 'cisco',      # this is the enable password
       'verbose': True         # optional, default False
       }
connection = ConnectHandler(**cisco_device)
output = connection.send_command('show version')
print(output)

connection.write_channel('show version\n')
time.sleep(2)
output = connection.read_channel()
print(output)
print('Closing connection')
connection.disconnect()

from netmiko import ConnectHandler

cisco_device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.10',
    'username': 'stavros',
    'password': 'cisco',
    'port': 22,
    'secret': 'cisco',
    'verbose': True
}

connection = ConnectHandler(**cisco_device)

print('Entering the enable mode ...')
connection.enable()


commands = ['access-list 101 permit tcp any any eq 80', 'access-list 101 permit tcp any any eq 443',
            'access-list 101 deny ip any any']

print('Sending commands to the device ...')
o = connection.send_config_set(commands)
print(o)


print(f'Disconnecting from {cisco_device["host"]}')
connection.disconnect()

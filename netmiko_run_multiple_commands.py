from netmiko import ConnectHandler

# devices = ['10.1.1.10', '192.168.122.20', '192.168.122.30']
# for dev in devices:
cisco_device = {
       'device_type': 'cisco_ios',
       # 'host': dev,
       'host': '192.168.1.10',
       'username': 'stavros',
       'password': 'cisco',
       'port': 22,             # optional, default 22
       'secret': 'cisco',      # this is the enable password
       'verbose': True         # optional, default False
       }
# for dev in devices:
connection = ConnectHandler(**cisco_device)
print('Entering the enable mode...')
connection.enable()

# this method receives a list of commands to send to the device
# in enters automatically into global config mode and exists automatically at the end
commands = ['int loopback 0', 'ip address 1.1.1.1 255.255.255.255', 'exit', 'username netmiko secret cisco']
output = connection.send_config_set(commands)
print(output)

## VARIATIONS
## 1.
cmd = 'ip ssh version 2;access-list 1 permit any;ip domain-name network-automation.io'
connection.send_config_set(cmd.split(';'))

## 2.
cmd = '''ip ssh version 2
access-list 1 permit any
ip domain-name net-auto.io
'''
connection.send_config_set(cmd.split('\n'))


# in enters automatically into global config mode and exists automatically at the end
print(connection.find_prompt())

connection.send_command('write memory')

print('Closing connection')
connection.disconnect()
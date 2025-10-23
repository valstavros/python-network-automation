
from netmiko import ConnectHandler
import threading
import time

def execute(device, command_list):
    connection = ConnectHandler(**device)
    connection.enable() # entering the enable mode
    output = connection.send_config_set(command_list)
    print(output)
    connection.disconnect()


# defining a dictionary for each device and a list of commands to execute on that device
router1 = { 'device_type': 'cisco_ios', 'host': '192.168.1.10', 'username': 'stavros', 'password': 'cisco',
            'port': 22, 'secret': 'cisco', 'verbose': True }
cmd1 = ['router ospf 1', 'network 0.0.0.0 0.0.0.0 area 0']

router2 = { 'device_type': 'cisco_ios', 'host': '192.168.1.20', 'username': 'stavros', 'password': 'cisco',
            'port': 22, 'secret': 'cisco', 'verbose': True }
cmd2 = ['int loopback 0', 'ip address 1.1.1.1 255.255.255.255', 'end', 'sh ip int loopback 0']


router3 = { 'device_type': 'cisco_ios', 'host': '192.168.1.30', 'username': 'stavros', 'password': 'cisco',
            'port': 22, 'secret': 'cisco', 'verbose': True }
cmd3 = ['username k9 secret abck9', 'ip domain-name k9']

# each element in the list is a tuple with 2 elements.
# the 1st element of the tuple is the dictionary which represents the device and the 2nd argument is a list
# of commands to execute on that device
routers = [(router1, cmd1), (router2, cmd2), (router3, cmd3)]

## Sequential execution
start = time.time()
for router in routers:
    try:
        execute(router[0], router[1])  # router[0] is the dictionary and router[1] is the list with commands
        end = time.time()
        print(f'Script execution time (SEQUENTIALLY): {end-start}')
    except Exception as e:
        print(f'An error occurred while connecting to {router[0]["host"]}: {e}')

## Concurrent execution
start = time.time()
threads = list()
try:
    for router in routers:
        th = threading.Thread(target=execute, args=(router[0], router[1]))
        threads.append(th)

    for th in threads:
        th.start()

    for th in threads:
        th.join()

    end = time.time()
    print(f'Script execution time (CONCURRENTLY): {end-start}')
except Exception as e:
    print(f'{e}\n')
    print(f'An error occurred while connecting to {router[0]["host"]}: {e}')
# Note: In concurrent execution, if one thread encounters an error, it won't affect the execution of other threads.
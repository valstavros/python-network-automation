from netmiko import ConnectHandler

# Define device parameters
cisco_device = {
    "device_type": "cisco_ios",
    # "host": "10.1.1.30",  # EVE-NG IP address
    "host": "192.168.1.20",  # GNS3 IP address
    "username": "stavros",
    "password": "cisco",
    "port": 22,  # Default SSH port
    "secret": "cisco",  # Enable password
    "verbose": True
    }
print(f"Connecting to {cisco_device['host']}")
# Establish SSH connection
net_connect = ConnectHandler(**cisco_device)

# Finding the prompt
prompter = net_connect.find_prompt()
if '>' in prompter:
    print("Entering enable mode..")
    net_connect.enable() # Enter enable mode

interface = input("Enter the interface to enable (e.g., e0/1): ")
# Check the interface status
output = net_connect.send_command(f"show ip interface {interface}")

if 'Invalid input detected' in output:
    print("You entered an invalid interface. Please check the interface name and try again.")
else:
    first_line = output.splitlines()[0]
    print(first_line)
    if not 'up' in first_line:
        print(f"The interface {interface} is down. Enabling it now...")
        commands = [
            f"interface {interface}",
            "no shutdown",
            "exit"
        ]
        output = net_connect.send_config_set(commands)
        print(output)
        print( '#' * 50 )
        print('The interface has been enabled.')
    else:
        print(f"The interface {interface} is already up.")

# Save the configuration
print("Saving the configuration...")
net_connect.send_command('write memory')
# Close the connection
print('Closing connection...')
net_connect.disconnect()

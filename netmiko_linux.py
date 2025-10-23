from netmiko import ConnectHandler
# import getpass
#
# passwd = getpass.getpass('Please enter the password: ')

# Define device parameters
linux_device = {
    "device_type": "linux",
    # "host": "10.1.1.30",  # EVE-NG IP address
    "host": "192.168.1.50",  # Parrot OS IP address
    "username": "pipitsa",
    "password": "pipitsa",  # Use the password obtained from getpass
    "port": '22',  # Default SSH port
    "secret": "pipitsa",  # Enable password
    "verbose": True
    }
print(f"Connecting to {linux_device['host']}")
# Establish SSH connection
connection = ConnectHandler(**linux_device)

connection.enable() # sudo su

# Send commands and capture output
output = connection.send_command("lsb_release -a")
print(f"Output:\n{output}\n")

# Close the connection
print('Closing connection ...')
connection.disconnect()

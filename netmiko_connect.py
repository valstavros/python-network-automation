from netmiko import ConnectHandler

# Define device parameters
cisco_device = {
    "device_type": "cisco_ios",
    "host": "10.1.1.30",  # EVE-NG IP address
    # "host": "192.168.1.10",  # GNS3 IP address
    "username": "stavros",
    "password": "cisco",
    "port": 22,  # Default SSH port
    "secret": "cisco",  # Enable password
    "verbose": True
    }
print(f"Connecting to {cisco_device['host']}")
# Establish SSH connection
connection = ConnectHandler(**cisco_device)

# Finding the prompt
prompt = connection.find_prompt()
print(f"Prompt is: {prompt}")
# print(f"Prompt is: {prompt[:-1]}")
if '>' in prompt:
    print("Entering enable mode..")
    connection.enable() # Enter enable mode


# Send commands and capture output
output = connection.send_command("sh arp")
print(output)

if not connection.check_config_mode():
    print("Entering configuration mode...")
    connection.config_mode()  # Enter configuration mode

prompt = connection.find_prompt()
print(f"Prompt is: {prompt}")

#Create a user with privilege level 15 and a secret password
# print("Creating a new user with privilege 15 and secret password")
# connection.send_command("username admin privilege 15 secret admin123")

# Exit configuration mode
print("Exiting configuration mode...")
connection.exit_config_mode()
# prompt = connection.find_prompt()
# print(f"Prompt is: {prompt}")

# Save the configuration
print("Saving the configuration...")
connection.send_command('write memory')
# Close the connection
print('Closing connection...')
connection.disconnect()

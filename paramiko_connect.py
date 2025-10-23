import time
import paramiko

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

router = {
    "hostname": "10.1.1.30", ## EVE-NG IP address
    "port": "22",
    "username": "stavros",
    "password": "cisco"
    }

print(f"Connecting to {router['hostname']}")

ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
print(ssh_client.get_transport().is_active())
shell = ssh_client.invoke_shell()
shell.send(b"terminal length 0\n")
shell.send(b"show version\n")
shell.send(b"show ip interface brief\n")
time.sleep(1)

output = shell.recv(10000)
output = output.decode('utf-8')
print(output)

if ssh_client.get_transport().is_active():
    print(f"Closing connection to {router['hostname']}\n")
    ssh_client.close()
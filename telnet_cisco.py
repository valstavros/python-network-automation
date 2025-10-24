import telnetlib3.telnetlib as telnetlib
import time
# import getpass

host = "10.1.1.30"
port = "23"
user = "stavros"
password = "cisco"
# password = getpass.getpass("Enter the password: ") # my code

tn = telnetlib.Telnet(host=host, port=port)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")

tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")

tn.write(b"terminal length 0\n")
# tn.write(password.encode('ascii') + b"\n") # my code
tn.write(b"show ip interface brief\n")
tn.write(b"enable\n")
# tn.write(password.encode('ascii') + b"\n") # my code
tn.write(b"cisco\n")
tn.write(b"show run\n")
tn.write(b'exit\n')
time.sleep(1)

output = tn.read_all()
output = output.decode('ascii')
print(output)

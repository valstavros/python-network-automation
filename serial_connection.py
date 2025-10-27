import serial
with serial.Serial(port='com3', baudrate=9600, parity='N',stopbits=1, bytesize=8, timeout=8) as console:
    if console.is_open:
        print('Console successfully opened!')
    else:
        print('Error opening the console connection')

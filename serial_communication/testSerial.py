import serial

ser = serial.Serial('/home/dev/ttyS0',9600, timeout = 1)
ser.open()

ser.write("testing")
try:
    while 1:
        response = ser.readline()
        print (response + "F")
except KeyboardInterrupt:
    ser.close()

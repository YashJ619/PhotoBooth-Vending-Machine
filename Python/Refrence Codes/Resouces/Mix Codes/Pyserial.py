# Importing Libraries
import serial
import time
avg = 0
i = 0
arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)
#def write_read(x):
    #arduino.write(bytes(x, 'utf-8'))
    #time.sleep(0.05)
  #  data = arduino.readline()
 #   return data
#while True:
#    num = input("Enter a number: ") # Taking input from user
#    value = write_read(num)
#    print(value) # printing the value
while True:
	data = arduino.readline()
	avg += int(data)
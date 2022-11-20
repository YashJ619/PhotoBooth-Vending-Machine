#----------------------------IMPORT PYSERIAL LIB------------------------------------------
import serial

#global uno
#----------------------------CONNECTION TO PORT-------------------------------------------
def connect():
    global uno
    try:
        uno=serial.Serial(port='com5',baudrate=115200,timeout=.1)
        print("Connected")
    except:
        print("Not Connected")
        ch = input("y/n")
        if ch == 'y':
            connect()
        else:
            return

connect()
#uno = serial.Serial(port='com5',baudrate=155200,timeout=0.1)
print(type(uno))

#-------------------------------TO WRITE DATA---------------------------------------------
#uno.write(bytes("Hello",'utf-8'))
#uno.write(bytes("Hello",encode()))

#-------------------------------TO READ DATA----------------------------------------------
#data = uno.readline()
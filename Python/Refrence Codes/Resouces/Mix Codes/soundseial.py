# Importing Libraries
from curses import baudrate
from tkinter import E
import serial
import time

maxsamples = 25
div = 10
level = 0.0

samples = maxsamples
avg = 0
i = 0

#-----------------------------PORT CONNECTION FOR ARDUINO MIC--------------------------
def connect_arduino_mic():
        global arduino_mic
        try:
                arduino_mic=serial.Serial(port='COM5',baudrate=115200)
                print("Arduino Mic Connected")
        except:
                print("Arduino Mic Not Connected retry (y/n)")
                ch = input()
                if ch == 'y' or ch == 'Y':
                        connect_arduino_mic()
                elif ch == 'n' or ch == 'N':
                        return
                else:
                        print("Invalid Input")
                        connect_arduino_mic()

#-----------------------------PORT CONNECTION FOR ARDUINO MAIN---------------------------
def connect_arduino_main():
        global arduino_main
        try:
                arduino_main=serial.Serial(port='COM7',baudrate=115200)
                print("Arduino Main Connected")
        except:
                print("Arduino Main Not Connected retry (y/n)")
                ch = input()
                if ch == 'y' or ch == 'Y':
                        connect_arduino_main()
                elif ch == 'n' or ch == 'N':
                        return
                else:
                        print("Invalid Input")
                        connect_arduino_main()

#---------------------------
def trigger(x):
        global level
        if x > level :
                print("Yes")
                arduino_main = serial.Serial(port='COM7', baudrate=115200)
                arduino_main.write(bytes("Hello", 'utf-8'))
                arduino_main.close()

arduino_mic = serial.Serial(port='COM5', baudrate=115200)

while True:
        data = arduino_mic.readline()
        str_rn = data.decode()
        stra = str_rn.rstrip()
        try:
                value = float(stra)
                if value < 0.0 :
                        value = abs(value)
                if value > 0 :
                        if samples > 0 :
                                samples = samples - 1
                                avg = avg + value
                                #print(value,end='x')
                                #print(avg,end='x')
                                #print(samples)
                        else :
                                samples = 25
                                avg = avg / div
                                print("Avg",end='')
                                print(avg)
                                trigger(avg)
                                avg = 0
        except:
                print("No",end='')

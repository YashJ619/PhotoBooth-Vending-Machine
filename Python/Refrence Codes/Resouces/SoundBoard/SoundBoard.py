#---------------------------------------IMPORT LIB-------------------------------------
from cProfile import label
import serial
import time
from tkinter import *

#--------------------------------------------------------------------------------------
def red1():
    global rake1_state
    btn1 = Button(control_window,text="Rake 1",padx=20,bg="red",command=green1)
    btn1.grid(row=0,column=0)
    rake1_state = 0
    print(rake1_state)
def green1():
    global rake1_state
    btn1 = Button(control_window,text="Rake 1",padx=20,bg="green",command=red1)
    btn1.grid(row=0,column=0)
    rake1_state = 1
    print(rake1_state)

def red2():
    global rake2_state
    btn2 = Button(control_window,text="Rake 2",padx=20,bg="red",command=green2)
    btn2.grid(row=1,column=0)
    rake2_state = 0
def green2():
    global rake2_state
    btn2 = Button(control_window,text="Rake 2",padx=20,bg="green",command=red2)
    btn2.grid(row=1,column=0)
    rake2_state = 1

def red3():
    global rake3_state
    btn3 = Button(control_window,text="Rake 3",padx=20,bg="red",command=green3)
    btn3.grid(row=2,column=0)
    rake3_state = 0
def green3():
    global rake3_state
    btn3 = Button(control_window,text="Rake 3",padx=20,bg="green",command=red3)
    btn3.grid(row=2,column=0)
    rake3_state = 1

def red4():
    global rake4_state
    btn4 = Button(control_window,text="Rake 4",padx=20,bg="red",command=green4)
    btn4.grid(row=3,column=0)
    rake4_state = 0
def green4():
    global rake4_state
    btn4 = Button(control_window,text="Rake 4",padx=20,bg="green",command=red4)
    btn4.grid(row=3,column=0)
    rake4_state = 1

def red5():
    global rake5_state
    btn5 = Button(control_window,text="Rake 5",padx=20,bg="red",command=green5)
    btn5.grid(row=4,column=0)
    rake5_state = 0
def green5():
    global rake5_state
    btn5 = Button(control_window,text="Rake 5",padx=20,bg="green",command=red5)
    btn5.grid(row=4,column=0)
    rake5_state = 1

def Apply():
	global com_mic,com_main,maxsample,divisor,level
	global rake1_obj,rake2_obj,rake3_obj,rake4_obj,rake5_obj
	global rake1_state,rake2_state,rake3_state,rake4_state,rake5_state
	rake1_obj = int(obj1.get())
	rake2_obj = int(obj2.get())
	rake3_obj = int(obj3.get())
	rake4_obj = int(obj4.get())
	rake5_obj = int(obj5.get())
	com_mic = obj6.get()
	com_main = obj7.get()
	maxsample = int(obj8.get())
	divisor = int(obj9.get())
	level = int(obj10.get())
	print(com_mic)
	print(com_main)
	print("Max Sample",+maxsample)
	print("Divisor",+divisor)
	print("Trigger Level",+level)
        
	if rake1_obj > 10 or rake2_obj > 10 or rake3_obj > 10 or rake4_obj > 10 or rake5_obj > 10:
		error = Label(control_window,text="Error",fg="red")
		error.grid(row=7,column=0)
		turnoff()
	else:
		error = Label(control_window,text="OK",fg="green")
		error.grid(row=7,column=0)
	status()
#-----------------------------PORT CONNECTION FOR ARDUINO MIC--------------------------
def connect_arduino_mic():
        global arduino_mic
        try:
                arduino_mic=serial.Serial(port=com_mic,baudrate=115200)
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
                arduino_main=serial.Serial(port=com_main,baudrate=115200)
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
#---------------------------------------------------------------------------------------
def status():
	global rake1_obj,rake2_obj,rake3_obj,rake4_obj,rake5_obj
	global rake1_state,rake2_state,rake3_state,rake4_state,rake5_state
	print("rake1_state",rake1_state,"rake1_obj",rake1_obj)
	print("rake2_state",rake2_state,"rake2_obj",rake2_obj)
	print("rake3_state",rake3_state,"rake3_obj",rake3_obj)
	print("rake4_state",rake4_state,"rake4_obj",rake4_obj)
	print("rake5_state",rake5_state,"rake5_obj",rake5_obj)

#---------------------------------------------------------------------------------------
def turnoff():
	global rake1_obj,rake2_obj,rake3_obj,rake4_obj,rake5_obj
	global rake1_state,rake2_state,rake3_state,rake4_state,rake5_state
	rake1_state = 0
	rake2_state = 0
	rake3_state = 0
	rake4_state = 0
	rake5_state = 0
	rake1_obj = 0
	rake2_obj = 0
	rake3_obj = 0
	rake4_obj = 0
	rake5_obj = 0

#----------------------------------Trigger Arduino Main---------------------------------
def trigger(x,y):
        global rake1_obj,rake2_obj,rake3_obj,rake4_obj,rake5_obj
        global rake1_state,rake2_state,rake3_state,rake4_state,rake5_state
        if x > y:
                if rake1_state == 1 and rake1_obj > 0:
                        print("rake1on")
                        rake1_obj-=1
                        arduino_main.write(bytes("rake1on", 'utf-8'))
                        status()
                elif rake2_state == 1 and rake2_obj > 0:
                        print("rake2on")
                        rake2_obj-=1
                        arduino_main.write(bytes("rake2on", 'utf-8'))
                        status()
                elif rake3_state == 1 and rake3_obj > 0:
                        print("rake3on")
                        rake3_obj-=1
                        arduino_main.write(bytes("rake3on", 'utf-8'))
                        status()
                elif rake4_state == 1 and rake4_obj > 0:
                        print("rake4on")
                        rake4_obj-=1
                        arduino_main.write(bytes("rake4on", 'utf-8'))
                        status()
                elif rake5_state == 1 and rake5_obj > 0:
                        print("rake5on")
                        rake5_obj-=1
                        arduino_main.write(bytes("rake5on", 'utf-8'))
                        status()
                else:
                        print("Error or Machine is Empty")
                        status()
                        turnoff()


#----------------------------------Get Data and Convert---------------------------------
def getdata():
        global value
        data = arduino_mic.readline()
        str_de = data.decode()
        str_rn = str_de.rstrip()
        try:
            value = float(str_rn)
            if value < 0.0:
                value = abs(value)
        except:
                return
#---------------------------------------------------------------------------------------
#-----------------------------------------Main Code-------------------------------------
# Declare variables to be used for Mic Board
com_mic = ""
avg = 0
maxsample = 0
divisor = 1
level = 0
current_sample = 0

# Declare variables to be used for Main Board
com_main = ""
rake1_obj = 0
rake1_state = 1

rake2_obj = 0
rake2_state = 1

rake3_obj = 0
rake3_state = 1

rake4_obj = 0
rake4_state = 1

rake5_obj = 0
rake5_state = 1

#--------------------------------------------------------------------------------------
control_window = Tk() # create window
control_window.minsize(width=500, height=500)
control_window.maxsize(width=500, height=500)

btn1 = Button(control_window,text="Rake 1",padx=20,bg="green",command=red1)
btn2 = Button(control_window,text="Rake 2",padx=20,bg="green",command=red2)
btn3 = Button(control_window,text="Rake 3",padx=20,bg="green",command=red3)
btn4 = Button(control_window,text="Rake 4",padx=20,bg="green",command=red4)
btn5 = Button(control_window,text="Rake 5",padx=20,bg="green",command=red5)

btn1.grid(row=0,column=0)
btn2.grid(row=1,column=0)
btn3.grid(row=2,column=0)
btn4.grid(row=3,column=0)
btn5.grid(row=4,column=0)

obj1 = Entry(control_window,width=5,borderwidth=5)
obj2 = Entry(control_window,width=5,borderwidth=5)
obj3 = Entry(control_window,width=5,borderwidth=5)
obj4 = Entry(control_window,width=5,borderwidth=5)
obj5 = Entry(control_window,width=5,borderwidth=5)

obj6 = Entry(control_window,width=10,borderwidth=5)
obj7 = Entry(control_window,width=10,borderwidth=5)

obj8 = Entry(control_window,width=10,borderwidth=5)
obj9 = Entry(control_window,width=10,borderwidth=5)
obj10 = Entry(control_window,width=10,borderwidth=5)

obj1.insert(0,"9")
obj2.insert(0,"9")
obj3.insert(0,"9")
obj4.insert(0,"9")
obj5.insert(0,"9")

obj6.insert(0,"COM5")
obj7.insert(0,"COM7")

obj1.grid(row=0,column=1)
obj2.grid(row=1,column=1)
obj3.grid(row=2,column=1)
obj4.grid(row=3,column=1)
obj5.grid(row=4,column=1)

obj6.grid(row=5,column=1)
obj7.grid(row=6,column=1)

obj8.grid(row=0,column=4)
obj9.grid(row=1,column=4)
obj10.grid(row=2,column=4)

label1 = Label(control_window,text="Max 10")
label2 = Label(control_window,text="Max 10")
label3 = Label(control_window,text="Max 10")
label4 = Label(control_window,text="Max 10")
label5 = Label(control_window,text="Max 10")

labelcom_mic = Label(control_window,text="Mic-P0RT = ")
labelcom_main = Label(control_window,text="Main-PORT = ")

label_maxsample = Label(control_window,text="Max Samples = ")
label_divisor = Label(control_window,text="divisor = ")
label_level = Label(control_window,text="Trigger Level = ")

label1.grid(row=0,column=2)
label2.grid(row=1,column=2)
label3.grid(row=2,column=2)
label4.grid(row=3,column=2)
label5.grid(row=4,column=2)

labelcom_mic.grid(row=5,column=0)
labelcom_main.grid(row=6,column=0)

label_maxsample.grid(row=0,column=3)
label_divisor.grid(row=1,column=3)
label_level.grid(row=2,column=3)

Apply = Button(control_window,text="Apply",padx=20,command=Apply)

Apply.grid(row=7,column=2)

#Connection of board
connect_arduino_mic()
connect_arduino_main()

#Hold Control Window
#mainloop()
#--------------------------------------Data Acquisition--------------------------------
while True:
        getdata()
        if value < 0.0 : #check for negative data     
                value = abs(value) #converts negative to positive
#---------------------------------------Data Sampling-----------------------------------                
        if value > 0.0 :
                current_sample = current_sample + 1
                avg = avg + value
        elif current_sample >= maxsample:
                avg = avg / divisor
                print("Avg",end='')
                print(avg)
                trigger(avg,level)
                current_sample = 0
                avg = 0
        elif current_sample > 0:
                current_sample = current_sample + 1

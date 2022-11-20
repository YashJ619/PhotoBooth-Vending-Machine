import serial
from tkinter import *

rake1_obj = 9
rake1_state = 1

rake2_obj = 9
rake2_state = 1

rake3_obj = 9
rake3_state = 1

rake4_obj = 9
rake4_state = 1

rake5_obj = 9
rake5_state = 1

port = "COM5"

def led_on():
     arduinoData.write('forward'.encode())
def led_off():
     arduinoData.write('off'.encode())

def red1():
     btn1 = Button(led_control_window,text="Rake 1",padx=20,bg="red",command=green1)
     btn1.grid(row=0,column=0)
     rake1_state = 0
     print(rake1_state)
def green1():
     btn1 = Button(led_control_window,text="Rake 1",padx=20,bg="green",command=red1)
     btn1.grid(row=0,column=0)
     rake1_state = 1
     print(rake1_state)

def red2():
     btn2 = Button(led_control_window,text="Rake 2",padx=20,bg="red",command=green2)
     btn2.grid(row=1,column=0)
     rake2_state = 0
def green2():
     btn2 = Button(led_control_window,text="Rake 2",padx=20,bg="green",command=red2)
     btn2.grid(row=1,column=0)
     rake2_state = 1

def red3():
     btn3 = Button(led_control_window,text="Rake 3",padx=20,bg="red",command=green3)
     btn3.grid(row=2,column=0)
     rake3_state = 0
def green3():
     btn3 = Button(led_control_window,text="Rake 3",padx=20,bg="green",command=red3)
     btn3.grid(row=2,column=0)
     rake3_state = 1

def red4():
     btn4 = Button(led_control_window,text="Rake 4",padx=20,bg="red",command=green4)
     btn4.grid(row=3,column=0)
     rake4_state = 0
def green4():
     btn4 = Button(led_control_window,text="Rake 4",padx=20,bg="green",command=red4)
     btn4.grid(row=3,column=0)
     rake4_state = 1

def red5():
     btn5 = Button(led_control_window,text="Rake 5",padx=20,bg="red",command=green5)
     btn5.grid(row=4,column=0)
     rake5_state = 0
def green5():
     btn5 = Button(led_control_window,text="Rake 5",padx=20,bg="green",command=red5)
     btn5.grid(row=4,column=0)
     rake5_state = 1

led_control_window = Tk() # create window
led_control_window.minsize(width=500, height=500)
led_control_window.maxsize(width=500, height=500)

btn1 = Button(led_control_window,text="Rake 1",padx=20,bg="green",command=red1)
btn2 = Button(led_control_window,text="Rake 2",padx=20,bg="green",command=red2)
btn3 = Button(led_control_window,text="Rake 3",padx=20,bg="green",command=red3)
btn4 = Button(led_control_window,text="Rake 4",padx=20,bg="green",command=red4)
btn5 = Button(led_control_window,text="Rake 5",padx=20,bg="green",command=red5)

btn1.grid(row=0,column=0)
btn2.grid(row=1,column=0)
btn3.grid(row=2,column=0)
btn4.grid(row=3,column=0)
btn5.grid(row=4,column=0)

#arduinoData = serial.Serial('com5', 115200)
#arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)
arduinoData = serial.Serial(port=port, baudrate=115200, timeout=.1)
mainloop()

# mylabel = Label(led_control_window, text="Hello")
#.pack() .grid(row=0,colum=0)
# root.mainloop()
#btn1 = Button(led_control_window,text="Rake 1",padx=20,pady=20,state=DISABLE,commad=myclick,fg="blue,bg="pink")





#def myclick():
#	mylabel = Label(root, text="Hello")
#	mylabel.pack()


# e = Entry(root,width=50,bg="blue",borderwidth=5,)
# e.get()
# e.insert(0, "Enter")






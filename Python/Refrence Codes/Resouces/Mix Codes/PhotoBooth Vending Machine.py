import serial
from tkinter import *

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

folder = ""
com = ""

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

def red1():
    global rake1_state
    btn1 = Button(led_control_window,text="Rake 1",padx=20,bg="red",command=green1)
    btn1.grid(row=0,column=0)
    rake1_state = 0
    print(rake1_state)
def green1():
    global rake1_state
    btn1 = Button(led_control_window,text="Rake 1",padx=20,bg="green",command=red1)
    btn1.grid(row=0,column=0)
    rake1_state = 1
    print(rake1_state)

def red2():
    global rake2_state
    btn2 = Button(led_control_window,text="Rake 2",padx=20,bg="red",command=green2)
    btn2.grid(row=1,column=0)
    rake2_state = 0
def green2():
    global rake2_state
    btn2 = Button(led_control_window,text="Rake 2",padx=20,bg="green",command=red2)
    btn2.grid(row=1,column=0)
    rake2_state = 1

def red3():
    global rake3_state
    btn3 = Button(led_control_window,text="Rake 3",padx=20,bg="red",command=green3)
    btn3.grid(row=2,column=0)
    rake3_state = 0
def green3():
    global rake3_state
    btn3 = Button(led_control_window,text="Rake 3",padx=20,bg="green",command=red3)
    btn3.grid(row=2,column=0)
    rake3_state = 1

def red4():
    global rake4_state
    btn4 = Button(led_control_window,text="Rake 4",padx=20,bg="red",command=green4)
    btn4.grid(row=3,column=0)
    rake4_state = 0
def green4():
    global rake4_state
    btn4 = Button(led_control_window,text="Rake 4",padx=20,bg="green",command=red4)
    btn4.grid(row=3,column=0)
    rake4_state = 1

def red5():
    global rake5_state
    btn5 = Button(led_control_window,text="Rake 5",padx=20,bg="red",command=green5)
    btn5.grid(row=4,column=0)
    rake5_state = 0
def green5():
    global rake5_state
    btn5 = Button(led_control_window,text="Rake 5",padx=20,bg="green",command=red5)
    btn5.grid(row=4,column=0)
    rake5_state = 1

def Apply():
	global path,com
	global rake1_obj,rake2_obj,rake3_obj,rake4_obj,rake5_obj
	global rake1_state,rake2_state,rake3_state,rake4_state,rake5_state
	rake1_obj = int(obj1.get())
	rake2_obj = int(obj2.get())
	rake3_obj = int(obj3.get())
	rake4_obj = int(obj4.get())
	rake5_obj = int(obj5.get())
	com = obj6.get()
	path = obj7.get()
	print(path)
	print(com)

	# arduino = serial.Serial(port=com, baudrate=115200, timeout=.1)

	if rake1_obj > 10 or rake2_obj > 10 or rake3_obj > 10 or rake4_obj > 10 or rake5_obj > 10:
		error = Label(led_control_window,text="Error",fg="red")
		error.grid(row=7,column=0)
		turnoff()
	else:
		error = Label(led_control_window,text="OK",fg="green")
		error.grid(row=7,column=0)
	status()
		
def status():
	global rake1_obj,rake2_obj,rake3_obj,rake4_obj,rake5_obj
	global rake1_state,rake2_state,rake3_state,rake4_state,rake5_state
	print("rake1_state",rake1_state,"rake1_obj",rake1_obj)
	print("rake2_state",rake2_state,"rake2_obj",rake2_obj)
	print("rake3_state",rake3_state,"rake3_obj",rake3_obj)
	print("rake4_state",rake4_state,"rake4_obj",rake4_obj)
	print("rake5_state",rake5_state,"rake5_obj",rake5_obj)
	
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

obj1 = Entry(led_control_window,width=5,borderwidth=5)
obj2 = Entry(led_control_window,width=5,borderwidth=5)
obj3 = Entry(led_control_window,width=5,borderwidth=5)
obj4 = Entry(led_control_window,width=5,borderwidth=5)
obj5 = Entry(led_control_window,width=5,borderwidth=5)

obj6 = Entry(led_control_window,width=10,borderwidth=5)
obj7 = Entry(led_control_window,width=20,borderwidth=5)


obj1.insert(0,"9")
obj2.insert(0,"9")
obj3.insert(0,"9")
obj4.insert(0,"9")
obj5.insert(0,"9")

obj6.insert(0,"COM6")
#obj5.insert(0,"C:\Users\RIIK10\Desktop\watch")

obj1.grid(row=0,column=1)
obj2.grid(row=1,column=1)
obj3.grid(row=2,column=1)
obj4.grid(row=3,column=1)
obj5.grid(row=4,column=1)

obj6.grid(row=5,column=1)
obj7.grid(row=6,column=1)

label1 = Label(led_control_window,text="Max 10")
label2 = Label(led_control_window,text="Max 10")
label3 = Label(led_control_window,text="Max 10")
label4 = Label(led_control_window,text="Max 10")
label5 = Label(led_control_window,text="Max 10")

labelcom = Label(led_control_window,text="P0RT = ")
labeldir = Label(led_control_window,text="Dir :")


label1.grid(row=0,column=2)
label2.grid(row=1,column=2)
label3.grid(row=2,column=2)
label4.grid(row=3,column=2)
label5.grid(row=4,column=2)

labelcom.grid(row=5,column=0)
labeldir.grid(row=6,column=0)

Apply = Button(led_control_window,text="Apply",padx=20,command=Apply)

Apply.grid(row=7,column=2)



#arduino = serial.Serial(port=com, baudrate=115200, timeout=.1)
#folder=str(obj7.get())

class OnMyWatch:
	global path
	# Set the directory on watch
	#watchDirectory = folder #C:/Users/RIIK10/Desktop/ThisFolder"

	def __init__(self):
		self.observer = Observer()

	def run(self):
		event_handler = Handler()
		self.observer.schedule(event_handler, path, recursive = True)
		self.observer.start()
		try:
			while True:
				time.sleep(5)
		except:
			self.observer.stop()
			print("Observer Stopped")

		self.observer.join()


class Handler(FileSystemEventHandler):

	@staticmethod
	def on_any_event(event):
		global rake1_obj,rake2_obj,rake3_obj,rake4_obj,rake5_obj
		global rake1_state,rake2_state,rake3_state,rake4_state,rake5_state
		if event.is_directory:
			return None
		elif event.event_type == 'created':
			# Event is created, you can process it now
			if rake1_state == 1 and rake1_obj > 0:
				print("rake1on")
				rake1_obj-=1
				arduino.write(bytes("rake1on", 'utf-8'))
				#data = arduino.readline()
				#print(data)
				status()
			elif rake2_state == 1 and rake2_obj > 0:
				print("rake2on")
				rake2_obj-=1
				arduino.write(bytes("rake2on", 'utf-8'))
				status()
			elif rake3_state == 1 and rake3_obj > 0:
				print("rake3on")
				rake3_obj-=1
				arduino.write(bytes("rake3on", 'utf-8'))
				status()
			elif rake4_state == 1 and rake4_obj > 0:
				print("rake4on")
				rake4_obj-=1
				arduino.write(bytes("rake4on", 'utf-8'))
				status()
			elif rake5_state == 1 and rake5_obj > 0:
				print("rake5on")
				rake5_obj-=1
				arduino.write(bytes("rake5on", 'utf-8'))
				status()
			else:
				print("Error or Machine is Empty")
				status()
				turnoff()
			
			time.sleep(5)
			#data = arduino.readline()
			#print(data) # printing the value

			#print("Hello")
			#print("Watchdog received created event - % s." % event.src_path)
		# elif event.event_type == 'modified':
			# Event is modified, you can process it now
		#	print("Watchdog received modified event - % s." % event.src_path)


if __name__ == '__main__':
     mainloop()
     arduino = serial.Serial(port=com, baudrate=115200, timeout=.1)
     watch = OnMyWatch()
     watch.run()

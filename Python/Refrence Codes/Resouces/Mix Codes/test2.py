import serial
from tkinter import *

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

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

def led_on():
        arduinoData.write('forward'.encode())
def led_off():
	arduinoData.write('off'.encode())

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


#arduino = serial.Serial(port='COM5', baudrate=115200, timeout=.1)

class OnMyWatch:
	# Set the directory on watch
	watchDirectory = "C:/Users/RIIK10/Desktop/ThisFolder"

	def __init__(self):
		self.observer = Observer()

	def run(self):
		event_handler = Handler()
		self.observer.schedule(event_handler, self.watchDirectory, recursive = True)
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
			elif rake2_state == 1 and rake2_obj > 0:
				print("rake2on")
				rake2_obj-=1
			elif rake3_state == 1 and rake3_obj > 0:
				print("rake3on")
				rake3_obj-=1
			elif rake4_state == 1 and rake4_obj > 0:
				print("rake4on")
				rake4_obj-=1
			elif rake5_state == 1 and rake5_obj > 0:
				print("rake5on")
				rake5_obj-=1
			else:
				print("Error")
			
			#arduino.write(bytes("forward", 'utf-8'))
			time.sleep(0.05)
			#data = arduino.readline()
			#print(data) # printing the value

			#print("Hello")
			#print("Watchdog received created event - % s." % event.src_path)
		# elif event.event_type == 'modified':
			# Event is modified, you can process it now
		#	print("Watchdog received modified event - % s." % event.src_path)


if __name__ == '__main__':
     mainloop()
     watch = OnMyWatch()
     watch.run()

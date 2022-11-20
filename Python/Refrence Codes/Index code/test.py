import serial
from tkinter import *

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

port = "COM5"
def led_on():
     arduino.write(bytes('forward','utf-8'))
def led_off():
        arduino.write(bytes('off','utf-8'))

led_control_window = Tk()
led_control_window.minsize(width=266, height=266)
led_control_window.maxsize(width=266, height=266)
btn = Button(led_control_window,text="led on",command=led_on)
btn2 = Button(led_control_window,text="led off",command=led_off)
btn.pack()
btn2.pack()


arduino = serial.Serial(port=port, baudrate=115200, timeout=.1)

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
		if event.is_directory:
			        return None
		elif event.event_type == 'created':
			# Event is created, you can process it now
			arduino.write(bytes("forward", 'utf-8'))
			time.sleep(0.05)
			data = arduino.readline()
			print(data) # printing the value

			#print("Hello")
			#print("Watchdog received created event - % s." % event.src_path)
		# elif event.event_type == 'modified':
			# Event is modified, you can process it now
		#	print("Watchdog received modified event - % s." % event.src_path)


if __name__ == '__main__':
     mainloop()
     watch = OnMyWatch()
     watch.run()
     

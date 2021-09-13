# importing all the modules
import timeconversion as tc
from tkinter import *
import json

with open('settings.json', 'r') as config:
	data = json.load(config)
	hours = int(data['hours']); minutes = int(data['minutes']); seconds = int(data['seconds'])

# defining the starting minutes and seconds
# using a json format-->settings.json to configure time



timer = tc.Convert(hours, minutes, seconds)


hours = int(timer[0])
minutes = int(timer[1])
seconds = int(timer[2])

lever = True # currently inactive
# lever: an on/off switch for the program

# tkinter essentials
root = Tk()
root.title('Coundown')
root.geometry('200x20')
root.wm_attributes("-topmost", 1)

# countdown function helps to run the timer
def Countdown():
	global hours, minutes, seconds
	if hours == minutes == seconds == 0:
		minutes = 'Time'; seconds = 'up'
		label_hrs.grid_forget()
		label_dot1.grid_forget()
		label_dot2.grid_forget()
		tc.Alarm()
	elif minutes == seconds == 0:
		hours -= 1
		minutes = seconds = 59
		# function given below aids repetation of the function
		root.after(1000, Countdown)
	elif seconds == 0:
		minutes -=1
		seconds = 59
		root.after(1000, Countdown)
	else:
		seconds -= 1
		# function given below aids repetation of the function
		root.after(1000, Countdown)

# code snippet within Countdown function
# to avoid single digit countdown number
	if len(str(seconds)) == 1:
		temp_sec = '0' + str(seconds)
	else:
		temp_sec = str(seconds)
	if len(str(minutes)) == 1:
		temp_min = '0' + str(minutes)
	else:
		temp_min = str(minutes)
	label_hrs.config(text = hours) # work in progress
	label_min.config(text = temp_min)
	label_sec.config(text = temp_sec)


# main structuring
canvas_home = Canvas(root)
canvas_home.pack()

label_hrs = Label(canvas_home, text = hours)
label_hrs.grid(row = 1, column =1)
label_dot1 = Label(canvas_home, text =':')
label_dot1.grid(row = 1, column =2)
label_min = Label(canvas_home, text = minutes)
label_min.grid(row = 1, column = 3)
label_dot2 = Label(canvas_home, text = ':')
label_dot2.grid(row = 1, column = 4)
label_sec = Label(canvas_home, text = seconds)
label_sec.grid(row = 1, column = 5)

# 1st function to start the chain reaction of the code
Countdown()

# tkinter essentials
root.mainloop()

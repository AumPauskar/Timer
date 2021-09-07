# importing all the modules
import timeconversion
from tkinter import *
import json

with open('config.json', 'r') as config:
	data = json.load(config)
	hours = int(data['hours']); minutes = int(data['minutes']); seconds = int(data['seconds'])

# defining the starting minutes and seconds
# using a json format-->config.json to configure time



timeconversion.Convert(hours, minutes, seconds)
print(hours, minutes, seconds)



'''
timeconversion.Convert(hours, minutes, seconds)
h = hours
m = minutes
s = seconds
'''
'''
lever = True # currently inactive
# lever: an on/off switch for the program

# tkinter essentials
root = Tk()
root.title('Coundown')
root.geometry('200x20')
root.wm_attributes("-topmost", 1)

# countdown function helps to run the timer
def Countdown():
	global minutes, seconds
	if minutes == 0 and seconds == 0:
		minutes = 'Time'; seconds = 'up'
		label_dot.grid_forget()
	elif seconds == 0:
		minutes -= 1
		seconds = 59
		# function given below aids repetation of the function
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
	label_min.config(text = temp_min)
	label_sec.config(text = temp_sec)


# main structuring
canvas_home = Canvas(root)
canvas_home.pack()

label_min = Label(canvas_home, text = minutes)
label_min.grid(row = 1, column = 1)
label_dot = Label(canvas_home, text = ':')
label_dot.grid(row = 1, column = 2)
label_sec = Label(canvas_home, text = seconds)
label_sec.grid(row = 1, column = 3)

# 1st function to start the chain reaction of the code
Countdown()

# tkinter essentials
root.mainloop()
'''
# Timer

## Modules used
Base: The Program is based on Python 3.x (made in Python 3.9),
note, if you don't have python 3 or use puython 2 then the program
will not run

Additional: tkinter, json

Modules needed to install: none

## Useage
- Starting the app
	1. To start the app click open the timer.py file which will automatically
	open a tkinter window and start a timer
	2. The timer will start from a predefined time and to change the time
	you can go to the next chapter of the document
- Changing the time
	1. To change the time open config.json and then three objects will be there
	namely hours, minutes and seconds
	2. If the user wants 1 hour of countdown time, you can do it these three ways
		- "hours": "1", "minutes": "00", "seconds": "00" or
		- "hours": "0", "minutes": "60", "seconds": "00" or
		- "hours": "0", "minutes": "00", "seconds": "3600"

## Errors
The program may encounter errors by only these factors
- JSON file syntax may be incorrect
- JSON file values may not be from ASCII 0-9
- timer.py/timerconversion.py modified
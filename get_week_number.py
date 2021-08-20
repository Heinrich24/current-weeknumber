import datetime
import ctypes
from datetime import date

# Declare current date variable
today = str(date.today())

# Calcualte the current week number based on today's date.
week_number = (datetime.date(date.today().year, date.today().month, date.today().day).isocalendar().week);

# Setup a variable to store the above mentioned varaibles so that we 
# can print it neatly in a text box.
pop_up_text = ("Week number = " + str(week_number) + "\nCurrent Date = " + str(today));

# Windows Pop up.
ctypes.windll.user32.MessageBoxW(0, str(pop_up_text), "Week Number Finder", 1)
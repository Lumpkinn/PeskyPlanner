import datetime
import calendar

#TODO: Get the time, and current month from the time module, and then pass it to the calendar to recognize the current date


#Make some special mark for the day, to make it more obvious to the user
CurrentDate = datetime.day
CurrentYear = datetime.year
CurrentMonth = datetime.month

calendar.month(CurrentYear, CurrentMonth)


#Takes input to set a date and time for an event
def SetEvent(EventName, EventDate, EventMonth, EventYear):
     pass
import datetime as date
import calendar
import json

#TODO: Also connect to GUI after you find a proper lib for it
#TODO: make given month show up as a NUMBER. you can't make the comparison if its the name of the month.
#TODO: Make some special mark for the day, to make it more obvious to the user

CurrentDate = (date.datetime.now()).day
CurrentYear = (date.datetime.now()).year
CurrentMonth = (date.datetime.now()).month
calendar.month(CurrentYear, CurrentMonth)
#list containing events. 
#TODO: Store list in seperate file, so data isn't lost between instances.
events = []



#class holding information pertaining to events.
class Event():
     
     #Constructor
     def __init__(self, EventName, EventDate, EventMonth, EventYear):
          self.EventName = EventName
          self.EventDate = EventDate
          self.EventMonth = EventMonth
          self.EventYear = EventYear
     
     #adds the events to a array containing the rest of the events.
     def CreateEvent(self):
          #store the passed values
          NewEvent = [self.EventName, self.EventMonth, self.EventDate, self.EventYear]
          events.append(NewEvent)
     
     #check if they're equal to the current date
     def CheckEvent(self):
          isEvent = False
          if int(self.EventMonth) == CurrentMonth and int(self.EventDate) == CurrentDate and int(self.EventYear) == CurrentYear:
               isEvent = True
          return isEvent 
     #Function for storing data to a json file.
     def StoreEventData(self):
          EventData = {"name":self.EventName, "Month":self.EventMonth, "date":self.EventDate, "year":self.EventYear}
          with open ('Events.json', 'a', encoding="utf-8") as file:
               file.write(",")
               json.dump(EventData, file, indent=2)

# TODO: recognize certain dates on calendar. Notably, the current date (blue), and subsequent events (random colors, excluding blue)
today = date.datetime.now()

#Testing
#this is TEMPORARY, mostly just to take user input. Will be removed later in favor of a GUI

UserEventName = input("Whats happening? ")
UserEventYear = input("What year is it happening in? ")
UserEventMonth = input("What month is it happening in? ")
UserEventDay = input("What day is it happening? ")

UserEvent = Event(UserEventName, UserEventDay, UserEventMonth, UserEventYear) 
UserEvent.CreateEvent()
UserEvent.StoreEventData()
print(events)
print(UserEvent.CheckEvent())
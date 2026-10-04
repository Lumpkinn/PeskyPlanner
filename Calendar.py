import datetime as date
import csv

today = date.datetime.now()
CurrentDate = (date.datetime.now()).day
#list containing events. 
#TODO: Store list in seperate file, so data isn't lost between instances.
events = []



#class holding information pertaining to events.
class Event():
     
     #Constructor (needs to take a time as well)
     def __init__(self, EventDate, EventTime, EventName):
          self.EventName = EventName
          self.EventDate = EventDate
          self.EventTime = EventTime
     
     #adds the events to a array containing the rest of the events.
     def CreateEvent(self):
          #store the passed values
          NewEvent = [self.EventName, self.EventDate, self.EventTime]
          events.append(NewEvent)
     

     def StoreEventData(self):
          #get the info from the .csv file
          info = {"Name":self.EventName, "Date":self.EventDate, "Time":self.EventTime}
          infoFieldNames = ["Name", "Date", "Time"]
          with open ("Events.csv", "a") as file:
               writer = csv.DictWriter(file, infoFieldNames)

               writer.writerow(info)
               
def getEventData(day):
          daydict = {"Monday": [] , "Tuesday":[], "Wednesday":[], "Thursday":[], "Friday":[], "Saturday":[], "Sunday":[]}
          with open("Events.csv", 'r') as file:
               reader = csv.DictReader(file)
               for row in reader:
                    if ((row.get("Date")).lower() == day.lower()):     
                         #have it get the info for each day, hold it in a seperate string, and return the specific string depending on the data
                         daydict[day].append((row.get("Name"), " at ", row.get("Time")))

                         #Moninfo = ("You have a " + row["Name"] + " happening at " +row.get("Time")+".")  
                    else:
                              info = "Nothing stored yet!"
          return (str(daydict[day]).replace("{","").replace("}","").replace("[","").replace("]","").replace("(","").replace(")","").replace(",","").replace("'","")+"\n")
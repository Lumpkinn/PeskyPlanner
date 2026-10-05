import customtkinter as ctk
import Calendar as cal
import datetime as dt

import random as rand

#instance of calendar.py for getting and using information
infogetter = cal
#list of days of the week for future reference
days = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]


#class that holds the info for each day of the week. it also holds the ctkTabview widget
class weektabs(ctk.CTkTabview):
     def __init__(self, master, **kwargs):
          super().__init__(master, **kwargs)
          #sets color of window
          self.configure(fg_color="DodgerBlue")
          #gets current time
          currentDay = dt.datetime.today().weekday()
          for i in days:
               self.add(i)
          self.set(days[int(currentDay)])
          self.grid(row=1,column=2,padx=20,pady=20)
          
          #TabInfo
          global SatInfolabel
          SatInfolabel = ctk.CTkLabel(master=self.tab(days[0]), text_color="DarkGoldenrod1", text=infogetter.getEventData(days[0]))
          SatInfolabel.grid(row=0, column=0, padx=20, pady=10)
          global SunInfolabel
          SunInfolabel = ctk.CTkLabel(master=self.tab(days[1]), text_color="DarkGoldenrod1", text=infogetter.getEventData(days[1]))
          SunInfolabel.grid(row=0, column=0, padx=20, pady=10)
          global MonInfolabel
          MonInfolabel = ctk.CTkLabel(master=self.tab(days[2]), text_color="DarkGoldenrod1", text= infogetter.getEventData(days[2]))
          MonInfolabel.grid(row=0, column=0, padx=20, pady=10)
          global TueInfolabel
          TueInfolabel = ctk.CTkLabel(master=self.tab(days[3]), text_color="DarkGoldenrod1", text= infogetter.getEventData(days[3]))
          TueInfolabel.grid(row=0, column=0, padx=20, pady=10)
          global WedInfolabel
          WedInfolabel = ctk.CTkLabel(master=self.tab(days[4]), text_color="DarkGoldenrod1", text= infogetter.getEventData(days[4]))
          WedInfolabel.grid(row=0, column=0, padx=20, pady=10)
          global ThuInfolabel
          ThuInfolabel = ctk.CTkLabel(master=self.tab(days[5]), text_color="DarkGoldenrod1", text= infogetter.getEventData(days[5]))
          ThuInfolabel.grid(row=0, column=0, padx=20, pady=10)
          global FriInfolabel
          FriInfolabel = ctk.CTkLabel(master=self.tab(days[6]), text_color="DarkGoldenrod1", text= infogetter.getEventData(days[6]))
          FriInfolabel.grid(row=0, column=0, padx=20, pady=10)

class popups():
     def StartUp():
          popupWindow=ctk.CTk()
          popupWindow.title("Welcome to Pesky Planner!")
          PopupText = ctk.CTkLabel(popupWindow, text= "Welcome to Pesky Planner! I hope you enjoy using the free version of this app! If you'd like to do without all the popups, please donate 1,600$ to my bank account! \n (Disclaimer: Please don't take any of the begging seriously, i just wanted to make it seem kinda annoying for the user, with how many popups show up constantly.)")
          PopupText.grid(row=0, column=0, padx=20, pady=20)
          popupWindow.mainloop()
     def OnAction():
          PopUPMessages = ["Hey, do you mind becoming a paid member of my service? I'll definetly take care of whatever you want me to, and ill do it promptly too!"," Hello, hope your having a good day!","I'm not interrupting anything, am I?","Hey, if you have time, i think you should give me like 300 dollars. Why? No reason. ","Gibe me money pls","please make a charitable donation to my bank account for nothing in return :)","I have a business proposition, we should start selling air to people, I think a good starting price would be 500 dollars an ounce.","I have a business proposition, we should start selling water to fish! Its not like they need it or anything...","Should I get into the RAM business and start selling sticks for 18 grand?","I'll let a billion unpaid interns die before I let this company go under!","I have a very interesting proposition. What if we take our extremely popular website that brings in all of our revenue.... offline? It'd save us like 10 dollars a month!"]
          AnnoyingMessage = rand.randint(0, 10)
          popupWindow = ctk.CTk()
          popupWindow.title("Just a moment of your time please...")
          PopupText = ctk.CTkLabel(popupWindow, text=PopUPMessages[AnnoyingMessage])
          PopupText.grid(row=1, column=1,padx=20, pady=20)
          popupWindow.mainloop
     def IncorrectInput():
          popupWindow=ctk.CTk()
          popupWindow.title("Oops!")
          PopupText = ctk.CTkLabel(popupWindow, text= "Make sure that you're inputting the information for your events in correctly!")
          PopupText.grid(row=0, column=0, padx=20, pady=20)
          popupWindow.mainloop()




class App(ctk.CTk):
     def __init__(self):
          #set a specific size for the window using customtkinter.set_widget_scaling(float_value) 
          super().__init__()
          self.configure(fg_color="alice blue")
          self.resizable(False, False)
          self.title("Pesky Planner")
          self.tabview = weektabs(master=self)
          self.tabview.grid(row=0, column=1,padx=20, pady=20)

          #Frame for holding input elements
          self.itemFrame = ctk.CTkFrame(self, fg_color="DarkGoldenrod1", border_color="dark blue")
          self.itemFrame.grid(row=0,column=0, padx=20, pady=20)

          #Text Entry Fields
          self.EventDayEntry = ctk.CTkOptionMenu(self.itemFrame, text_color="dark blue", values=["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"])
          self.EventInfoEntry = ctk.CTkEntry(self.itemFrame, state="normal", text_color="dark blue", placeholder_text="What's happening?")
          self.EventTimeEntry = ctk.CTkEntry(self.itemFrame, state="normal", text_color="dark blue", placeholder_text="What time?")          
          self.EventDayEntry.grid(row=1, column=0, padx=20, pady=20)
          self.EventInfoEntry.grid(row=2, column=0, padx=20, pady=20)
          self.EventTimeEntry.grid(row=3, column=0, padx=20, pady=20)
          
          #Button for submitting elements 
          self.button = ctk.CTkButton(self.itemFrame, text="Add Event", text_color="blue",command=self.button_callBack)
          self.button.grid(row=0, column=0, padx=20, pady=20)
          
          SatInfolabel.configure(text=infogetter.getEventData(days[0]))
          SunInfolabel.configure(text=infogetter.getEventData(days[1]))
          MonInfolabel.configure(text=infogetter.getEventData(days[2]))
          TueInfolabel.configure(text=infogetter.getEventData(days[3]))
          WedInfolabel.configure(text=infogetter.getEventData(days[4]))
          ThuInfolabel.configure(text=infogetter.getEventData(days[5]))
          FriInfolabel.configure(text=infogetter.getEventData(days[6]))
          popups.StartUp()
         
     def button_callBack(self):
      #uses calendar.py to store the info to a .json
          date = self.EventDayEntry.get()
          time = self.EventTimeEntry.get()
          name = self.EventInfoEntry.get()
          #what you need to do rn is just iterate through days, check if date is there (make sure to account for case!) and let them through if it is. after that, project is finished

          eventcal = cal.Event(date, time, name)
          eventcal.CreateEvent()
          #Method is NOT finished, go do that
          eventcal.StoreEventData()
          for i in range (1, rand.randint(1, 5)):
               popups.OnAction()
          
         
          #Updating labels to show new events! Might wanna beautify this a little, but its completely functional!
          SatInfolabel.configure(text=infogetter.getEventData(days[0]))
          SunInfolabel.configure(text=infogetter.getEventData(days[1]))
          MonInfolabel.configure(text=infogetter.getEventData(days[2]))
          TueInfolabel.configure(text=infogetter.getEventData(days[3]))
          WedInfolabel.configure(text=infogetter.getEventData(days[4]))
          ThuInfolabel.configure(text=infogetter.getEventData(days[5]))
          FriInfolabel.configure(text=infogetter.getEventData(days[6]))
    
app = App()
app.mainloop()
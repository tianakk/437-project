# Event Management System

# Features :
# 1. Create An Event
# 2. View Events
# 3. Book Ticket
# 4. View Ticket
# 5. Condition Check If Customer Already Buy Same Event Ticket
# 6. Condition Check if All Tickets are sold Out.
# 7. Show Overall Event Summary

import pickle   #Python pickle module is used for serializing and de-serializing a Python object structure
import os
import pathlib
from Ticket import Ticket


############################ Create Event Class


class Event:
    eventname = ''
    eventcode = ''
    eventTotalAvaibleSeat = 10

    def createEvent(self):
        self.eventname= input("Enter Event Name: ")
        self.eventcode = input("Enter Event Code: ")
        self.eventTotalAvaibleSeat = input("Enter Event Total Availble Seats: ")
        print("\n\n ------> Event Created!")




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
from abc import ABC, abstractmethod


# Create Event Interface


class Events(ABC):
    eventname = ''
    eventcode = ''
    eventTotalAvaibleSeat = 10

    @abstractmethod
    def createEvent(self, eventType):
        pass
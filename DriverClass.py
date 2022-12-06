############################################## Main Program Modules

# Book Ticket and Check Condition
import os
import pathlib
import pickle

from Events import Events
from NetworkingEvent import NetworkingEvent
from PartyEvent import PartyEvent
from WorkshopEvent import WorkshopEvent
from CharityEvent import CharityEvent
from Ticket import Ticket
from prettytable import PrettyTable


def bookEventTicket():
    ticket = Ticket()
    ticket.bookTicket()
    if ticket.check():
        print("Warning : You Already Book A Seat")

    elif ticket.getBookedSeatCount() >= ticket.gettotalticketcount():
        print("Warning : All Ticket Sold Out")

    else:
        print("Sucess : Ticket Booked!")
        saveTicketDetails(ticket)

# Save Ticket Detials to File

def saveTicketDetails(ticket):
    file = pathlib.Path("tickets.data")
    if file.exists():
        if os.path.getsize(file) > 0:
            infile = open('tickets.data', 'rb')
            oldlist = pickle.load(infile)
            oldlist.append(ticket)
            infile.close()
            os.remove('tickets.data')
    else:
        oldlist = [ticket]
    outfile = open('tempTicket.data', 'wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('tempTicket.data', 'tickets.data')


# Display Saved Ticket Details

def getTicketDetails():
    file = pathlib.Path("tickets.data")
    if os.path.getsize(file) > 0:
        infile = open('tickets.data','rb')
        ticketdetails = pickle.load(infile)
        print("---------------TICKET DETAILS---------------------")
        t = PrettyTable(['T-Ref', 'C-Name', 'C-Email', 'E-Code'])
        for ticket in ticketdetails :
            t.add_row([ticket.reference, ticket.name, ticket.email, ticket.event])
        print(t)
        infile.close()
        print("--------------------------------------------------")
        input('Press Enter To Return To Main Menu')
    else :
        print("NO TICKET RECORDS FOUND")

# Create Event Module

def createCharityEvent():
    event = CharityEvent()
    event.createEvent()
    saveEventDetails(event)

def createPartyEvent():
    event = PartyEvent()
    event.createEvent()
    saveEventDetails(event)

def createNetworkingEvent():
    event = NetworkingEvent()
    event.createEvent()
    saveEventDetails(event)

def createWorkshopEvent():
    event = WorkshopEvent()
    event.createEvent()
    saveEventDetails(event)
# Save Event Details to File

def saveEventDetails(event):
    file = pathlib.Path("events2.data")
    if file.exists():
        infile = open('events2.data', 'rb')
        oldlist = pickle.load(infile)
        oldlist.append(event)
        infile.close()
        os.remove('events2.data')
    else:
        oldlist = [event]
    outfile = open('tempevents.data', 'wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('tempevents.data', 'events2.data')

# Display All Event Details

def getEventsDetails():
    file = pathlib.Path("events2.data")
    if file.exists ():
        infile = open('events2.data','rb')
        eventsdetails = pickle.load(infile)
        print("---------------EVENT DETAILS---------------------")
        t = PrettyTable(['E-Name', 'E-Code', 'E-Total-Seats', 'E-Type'])
        for events in eventsdetails :
            t.add_row([events.eventname, events.eventcode, events.eventTotalAvaibleSeat, events.eventType])
        print(t)
        infile.close()
        print("--------------------------------------------------")
        input('Press Enter To Return To Main Menu')
    else :
        print("NO EVENTS RECORDS FOUND")

# Display Reports About Events

def getEventsSummary():
    filetickets = pathlib.Path("tickets.data")
    if os.path.getsize(filetickets) > 0 :
        infiletickets = open('tickets.data', 'rb')
        ticketdetails = pickle.load(infiletickets)


        fileEvents = pathlib.Path("events2.data")
        if fileEvents.exists ():
            infileEvents = open('events2.data','rb')
            eventdetails = pickle.load(infileEvents)


            print("---------------REPORTS---------------------")
            for events in eventdetails :
                print("\n\nEvent Name : " + events.eventname + " | Total Seats : " + events.eventTotalAvaibleSeat + " \n")
                for ticket in ticketdetails:
                    if events.eventcode == ticket.event:
                        print(ticket.reference, "\t", ticket.name, "\t", ticket.email)

            infileEvents.close()
            infiletickets.close()

            print("--------------------------------------------------")
            input('Press Enter To Return To Main Menu')
        else :
            print("NO EVENTS RECORDS FOUND")


def createEvents():
    ch = ''
    num = 0
    while ch != 8:
        print("\t\t\t\t-----------------------")
        print("\t\t\t\tEVENT MANAGEMENT SYSTEM")
        print("\t\t\t\t-----------------------")
        print("\tEVENT CREATION MENU")
        print("\t1. CREATE CHARITY EVENT")
        print("\t2. CREATE NETWORKING EVENT")
        print("\t3. CREATE PARTY EVENT")
        print("\t4. CREATE WORKSHOP EVENT")
        print("\t5. BACK TO MAIN MENU")
        print("\tSelect Your Option (1-5) ")
        ch = input()

        if ch == '1':
            createCharityEvent()
        elif ch == '2':
            createNetworkingEvent()
        elif ch == '3':
            createPartyEvent()
        elif ch == '4':
            createWorkshopEvent()
        elif ch == '5':
            mainMenu()

def mainMenu():

    ch = ''
    num = 0
    while ch != 8:
        print("\t\t\t\t-----------------------")
        print("\t\t\t\tEVENT MANAGEMENT SYSTEM")
        print("\t\t\t\t-----------------------")
        print("\tMAIN MENU")
        print("\t1. BOOK TICKET")
        print("\t2. VIEW TICKETS")
        print("\t3. CREATE EVENT")
        print("\t4. VIEW EVENTS")
        print("\t5. SHOW SUMMARY")
        print("\tSelect Your Option (1-5) ")
        ch = input()

        if ch == '1':
            bookEventTicket()
        elif ch == '2':
            getTicketDetails()
        elif ch == '3':
            createEvents()
        elif ch == '4':
            getEventsDetails()
        elif ch == '5':
            getEventsSummary()



###################################################### Start Program
if __name__ == '__main__':
    mainMenu()

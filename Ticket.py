############################### Book a Ticket Class
import os
import pathlib
import pickle


class Ticket:
    name = ''
    email = ''
    event = ''
    reference = 200000

    def bookTicket(self):
        self.name= input("Enter Customer Name: ")
        self.email = input("Enter Customer Email: ")
        file = pathlib.Path("events2.data")
        if file.exists():
            infile = open('events2.data', 'rb')
            eventdetails = pickle.load(infile)

            self.reference = input("Enter Reference Code(10000 - 50000) : ")
            while True:
                if int(self.reference) <= 10000:
                    print("Warning: Please Enter Valid Reference Code")
                    self.reference = input("Enter Reference Code(10000 - 50000) : ")
                else:
                    break

            for event in eventdetails:
                print("Available Event Code : " + event.eventcode + " Event Name : " + event.eventname)
            infile.close()
        self.event = input("Enter Event Code: ")


    def check(self):
        file = pathlib.Path("tickets.data")
        if file.exists():
            if os.path.getsize(file) :
                infile = open('tickets.data', 'rb')
                ticketdetails = pickle.load(infile)
                for ticket in ticketdetails:
                    if ticket.email == self.email and ticket.event == self.event:
                        return True
                infile.close()


    def gettotalticketcount(self):
        file = pathlib.Path("events2.data")
        if file.exists():
            infile = open('events2.data', 'rb')
            eventdetails = pickle.load(infile)
            for event in eventdetails:
                if event.eventcode == self.event:
                    return int(event.eventTotalAvaibleSeat)
            infile.close
        else:
            return 0

    def getBookedSeatCount(self):
        file = pathlib.Path("tickets.data")
        counter= 0
        if file.exists():
            if os.path.getsize(file) > 0 :
                infile = open('tickets.data', 'rb')
                ticketdetails = pickle.load(infile)
                for ticket in ticketdetails:
                    if ticket.event == self.event:
                        counter = counter + 1
                return int(counter)
                infile.close()
        return 0


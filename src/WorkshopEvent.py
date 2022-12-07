from src.Events import Events


class WorkshopEvent(Events):
    eventname = ''
    eventcode = ''
    eventTotalAvaibleSeat = 10
    eventType = ''

    def createEvent(self):
        self.eventType = "Workshop"
        print("You are creating a Workshop Event")
        self.eventname = input("Enter Event Name: ")
        self.eventcode = input("Enter Event Code: ")
        self.eventTotalAvaibleSeat = input("Enter Event Total Availble Seats: ")
        print("\n\n ------> Event Created!")

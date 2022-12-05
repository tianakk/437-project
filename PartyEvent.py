from Events import Events


class PartyEvent(Events):
    eventname = ''
    eventcode = ''
    eventTotalAvaibleSeat = 10

    def __init__(self):
        self.eventType = None

    def createEvent(self):
        self.eventType = "You are creating a Party Event"
        self.eventname = input("Enter Event Name: ")
        self.eventcode = input("Enter Event Code: ")
        self.eventTotalAvaibleSeat = input("Enter Event Total Availble Seats: ")
        print("\n\n ------> Event Created!")

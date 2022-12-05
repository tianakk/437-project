from Events import Events

class NetworkingEvent(Events):


    eventname = ''
    eventcode = ''
    eventTotalAvaibleSeat = 10
    eventType = ''

    def createEvent(self):
        self.eventType = "Networking"
        print("You are creating a Networking Event")
        self.eventname = input("Enter Event Name: ")
        self.eventcode = input("Enter Event Code: ")
        self.eventTotalAvaibleSeat = input("Enter Event Total Availble Seats: ")

        print("\n\n ------> Event Created!")


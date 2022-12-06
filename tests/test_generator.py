import unittest
from unittest import mock

import DriverClass
from CharityEvent import CharityEvent
from NetworkingEvent import NetworkingEvent
from PartyEvent import PartyEvent
from WorkshopEvent import WorkshopEvent
from Ticket import Ticket


class MyTestCase(unittest.TestCase):


    @mock.patch('CharityEvent.input', create=True)
    def test_create_charity_event(self, mocked_input):
        mocked_input.side_effect = ["CharityEvent", "500", "10"]
        CharityEvent.createEvent(self)
        expected_event = ["Charity", "CharityEvent", "500", "10"]
        self.assertEqual([self.eventType, self.eventname, self.eventcode, self.eventTotalAvaibleSeat], expected_event)

    @mock.patch('NetworkingEvent.input', create=True)
    def test_create_networking_event(self, mocked_input):
        mocked_input.side_effect = ["NetworkingEvent", "501", "10"]
        NetworkingEvent.createEvent(self)
        expected_event = ["Networking", "NetworkingEvent", "501", "10"]
        self.assertEqual([self.eventType, self.eventname, self.eventcode, self.eventTotalAvaibleSeat], expected_event)

    @mock.patch('PartyEvent.input', create=True)
    def test_create_party_event(self, mocked_input):
        mocked_input.side_effect = ["PartyEvent", "502", "10"]
        PartyEvent.createEvent(self)
        expected_event = ["Party", "PartyEvent", "502", "10"]
        self.assertEqual([self.eventType, self.eventname, self.eventcode, self.eventTotalAvaibleSeat], expected_event)

    @mock.patch('WorkshopEvent.input', create=True)
    def test_create_workshop_event(self, mocked_input):
        mocked_input.side_effect = ["WorkshopEvent", "503", "10"]
        WorkshopEvent.createEvent(self)
        expected_event = ["Workshop", "WorkshopEvent", "503", "10"]
        self.assertEqual([self.eventType, self.eventname, self.eventcode, self.eventTotalAvaibleSeat], expected_event)

    @mock.patch('Ticket.input', create=True)
    def test_book_ticket(self, mocked_input):
        mocked_input.side_effect = ["Emma", "Emma@mail.com", "10001", "500"]
        Ticket.bookTicket(self)
        expected_ticket = ["Emma", "Emma@mail.com", "10001", "500"]
        self.assertEqual([self.name, self.email, self.reference, self.event], expected_ticket)

    @mock.patch('DriverClass.input', create=True)
    def test_get_event_details(self, mocked_input):
        mocked_input.side_effect = [""]
        DriverClass.getEventsDetails()
        self.assertEqual(True, True)

    @mock.patch('DriverClass.input', create=True)
    def test_get_ticket_details(self, mocked_input):
        mocked_input.side_effect = [""]
        DriverClass.getTicketDetails()
        self.assertEqual(True, True)

    @mock.patch('DriverClass.input', create=True)
    def test_get_events_summary(self, mocked_input):
        mocked_input.side_effect = [""]
        DriverClass.getEventsSummary()
        self.assertEqual(True, True)

    @mock.patch('CharityEvent.input', create=True)
    def test_driver_create_char_event(self, mocked_input):
        mocked_input.side_effect = ["CharityEvent", "500", "10"]
        DriverClass.createCharityEvent()
        self.assertEqual(True, True)

    @mock.patch('NetworkingEvent.input', create=True)
    def test_driver_create_networking_event(self, mocked_input):
        mocked_input.side_effect = ["NetworkingEvent", "501", "10"]
        DriverClass.createNetworkingEvent()
        self.assertEqual(True, True)

    @mock.patch('PartyEvent.input', create=True)
    def test_create_driver_party_event(self, mocked_input):
        mocked_input.side_effect = ["PartyEvent", "502", "10"]
        DriverClass.createPartyEvent()
        self.assertEqual(True, True)

    @mock.patch('WorkshopEvent.input', create=True)
    def test_create_driver_workshop_event(self, mocked_input):
        mocked_input.side_effect = ["WorkshopEvent", "503", "10"]
        DriverClass.createWorkshopEvent()
        self.assertEqual(True, True)

    @mock.patch('Ticket.input', create=True)
    def test_driver_book_ticket(self, mocked_input):
        mocked_input.side_effect = ["Emma", "Emma@mail.com", "10001", "500"]
        DriverClass.bookEventTicket()
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()

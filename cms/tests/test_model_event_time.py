from django.test import TestCase
from datetime import date, time

from cms.models import EventTime

from .setup import (admin_user_setup, event_setup, general_address_setup,
                    member_address_setup, ministry_setup, user_setup)


class EventTimeModelTests(TestCase):

    def setUp(self):
        self.user = user_setup()
        self.admin_user = admin_user_setup()
        self.member_address = member_address_setup(self.user)
        self.general_address = general_address_setup(self.admin_user)
        self.ministry = ministry_setup(
            self.member_address, self.general_address)
        self.event = event_setup(
            self.ministry, self.member_address, self.general_address)

    def test_event_time_created(self):
        test_event_time = EventTime(
            Event=self.event,
            start_date=date(year=2022, month=4, day=19),
            end_date=date(year=2022, month=4, day=19),
            start_time=time(hour=12, minute=30),
            end_time=time(hour=14, minute=30)
        )
        test_event_time.save()

        queried_event_time = EventTime.objects.get(id=1)

        self.assertEqual(test_event_time.Event, queried_event_time.Event)
        self.assertEqual(test_event_time.start_time,
                         queried_event_time.start_time)
        self.assertEqual(test_event_time.end_time, queried_event_time.end_time)
        self.assertEqual(test_event_time.start_date,
                         queried_event_time.start_date)
        self.assertEqual(test_event_time.end_date, queried_event_time.end_date)

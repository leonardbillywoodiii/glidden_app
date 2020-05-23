from django.test import TestCase
from faker import Faker

from cms.models import EventTime

from .setup import (admin_user_setup, general_address_setup,
                    member_address_setup, ministry_setup, user_setup, event_setup)


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

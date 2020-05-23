from django.test import TestCase
from faker import Faker

from cms.models import Event

from .setup import (admin_user_setup, general_address_setup,
                    member_address_setup, ministry_setup, user_setup)


class EventModelTests(TestCase):

    def setUp(self):
        self.user = user_setup()
        self.admin_user = admin_user_setup()
        self.member_address = member_address_setup(self.user)
        self.general_address = general_address_setup(self.admin_user)
        self.ministry = ministry_setup(
            self.member_address, self.general_address)

    def test_event_created(self):
        faker = Faker('en_US')
        test_event = Event(
            Ministry=self.ministry,
            description=faker.paragraph(2, True, None),
            GeneralAddress=self.general_address,
            MemberAddress=self.member_address
        )

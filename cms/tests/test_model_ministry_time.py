from django.test import TestCase
from datetime import time, date

from cms.models import MinistryTime

from .setup import (admin_user_setup, general_address_setup,
                    member_address_setup, user_setup, ministry_setup)


class MinisteryTimeModelTests(TestCase):

    def setUp(self):
        self.user = user_setup()
        self.admin_user = admin_user_setup()
        self.member_address = member_address_setup(self.user)
        self.general_address = general_address_setup(self.admin_user)
        self.ministry = ministry_setup(
            self.member_address, self.general_address)

    def test_ministry_time_created(self):
        test_ministry_time = MinistryTime(
            Ministry=self.ministry,
            start_date=date(year=2020, month=6, day=15),
            end_date=date(year=2020, month=6, day=15),
            start_time=time(hour=10, minute=30),
            end_time=time(hour=12, minute=30)
        )
        test_ministry_time.save()

        queried_ministry_time = MinistryTime.objects.get(id=1)

        self.assertEqual(self.ministry, queried_ministry_time.Ministry)
        self.assertEqual(test_ministry_time.start_date,
                         queried_ministry_time.start_date)
        self.assertEqual(test_ministry_time.end_date,
                         queried_ministry_time.end_date)
        self.assertEqual('N/A', queried_ministry_time.day_of_week)
        self.assertEqual('N/A', queried_ministry_time.day_of_month)
        self.assertEqual(0, queried_ministry_time.day_of_year)
        self.assertEqual(test_ministry_time.start_time,
                         queried_ministry_time.start_time)
        self.assertEqual(test_ministry_time.end_time,
                         queried_ministry_time.end_time)

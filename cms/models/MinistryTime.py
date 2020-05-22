from django.db import models
from .Ministry import Ministry


class MinistryTime(models.Model):
    Ministry = models.ForeignKey(Ministry, on_delete=models.CASCADE)
    start_date = models.DateField(
        auto_now=False, auto_now_add=False, default=None)
    end_date = models.DateField(
        auto_now=False, auto_now_add=False, default=None)
    DAY_OF_WEEK_CHOICES = [('Sun', 'Sunday'), ('Mon', 'Monday'),
                           ('Tues', 'Tuesday'), ('Wed', 'Wednesday'),
                           ('Thurs', 'Thursday'), ('Fri', 'Friday'),
                           ('Sat', 'Saturday'), ('N/A', 'N/A')]
    day_of_week = models.CharField(
        max_length=5, choices=DAY_OF_WEEK_CHOICES, default='N/A')
    day_of_month = models.CharField(max_length=100, default='N/A')
    day_of_year = models.SmallIntegerField(default=0)
    start_time = models.TimeField()
    end_time = models.TimeField()

    REQUIRED_FIELDS = [
        'start_time',
        'end_time'
    ]

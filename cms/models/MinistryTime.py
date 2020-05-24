from django.db import models


class MinistryTime(models.Model):
    Ministry = models.ForeignKey('Ministry', on_delete=models.CASCADE)
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = [
        'start_time',
        'end_time'
    ]

    def __str__(self):
        if self.start_date is not None:
            ministry_time_str = self.start_date + ' - '
            ministry_time_str += self.end_date + '\n'
        elif self.day_of_week != 'N/A':
            ministry_time_str = self.day_of_week + 's\n'
        elif self.day_of_month != 'N/A':
            if self.day_of_month == 1 or 21 or 31:
                ministry_time_str = self.day_of_month + 'st of every month\n'
            elif self.day_of_month == 2 or 22:
                ministry_time_str = self.day_of_month + 'nd of every month\n'
            elif self.day_of_month == 3 or 23:
                ministry_time_str = self.day_of_month + 'rd of every month\n'
            else:
                ministry_time_str = self.day_of_month + 'th of every month\n'
        else:
            ministry_time_str = self.day_of_year + ' day of every year\n'

        ministry_time_str += '@ ' + self.start_time + ' till ' + self.end_time

        return ministry_time_str

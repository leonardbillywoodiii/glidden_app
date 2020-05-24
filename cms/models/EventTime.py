from django.db import models


class EventTime(models.Model):
    Event = models.ForeignKey('Event', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    REQUIRED_FIELDS = [
        'Event',
        'start_date',
        'end_date',
        'start_time',
        'end_time'
    ]

    def __str__(self):
        event_time_str = self.start_date
        if self.end_date is not self.start_date:
            event_time_str += ' through ' + self.end_date
        event_time_str += '\n@' + self.start_time + ' - ' + self.end_time

        return event_time_str

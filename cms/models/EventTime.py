from django.db import models


from .Event import Event


class EventTime(models.Model):
    Event = models.ForeignKey(Event, on_delete=models.CASCADE)
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

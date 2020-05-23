from django.db import models
from .GeneralAddress import GeneralAddress
from .MemberAddress import MemberAddress
from .Ministry import Ministry


class Event(models.Model):
    Ministry = models.ForeignKey(Ministry, on_delete=models.CASCADE)
    description = models.TextField()
    GeneralAddress = models.ForeignKey(
        GeneralAddress, on_delete=models.DO_NOTHING, blank=True, null=True)
    MemberAddress = models.ForeignKey(
        MemberAddress, on_delete=models.DO_NOTHING, blank=True, null=True)

    REQUIRED_FIELDS = [
        'Ministry',
        'description'
    ]

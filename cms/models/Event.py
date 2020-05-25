from django.db import models


class Event(models.Model):
    Ministry = models.ForeignKey('Ministry', on_delete=models.CASCADE)
<<<<<<< HEAD
=======
    name = models.CharField(max_length=150)
>>>>>>> master
    description = models.TextField()
    GeneralAddress = models.ForeignKey(
        'GeneralAddress', on_delete=models.DO_NOTHING, blank=True, null=True)
    MemberAddress = models.ForeignKey(
        'MemberAddress', on_delete=models.DO_NOTHING, blank=True, null=True)
<<<<<<< HEAD
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
=======
>>>>>>> master

    REQUIRED_FIELDS = [
        'Ministry',
        'description',
        'name'
    ]

    def __str__(self):
        event_str = self.name + '\n'
        event_str += self.description + '\n'
        if self.GeneralAddress is not None:
            event_str += str(self.GeneralAddress)
        else:
            event_str += str(self.MemberAddress)

        return event_str

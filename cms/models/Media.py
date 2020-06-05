from django.db import models
from django.conf import settings

import os


class Media(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    media_file = models.FileField()
    UserProfile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def delete_media_file(self):
        path = settings.MEDIA_ROOT + self.media_file.name
        if os.path.isfile(path):
            os.remove(path)

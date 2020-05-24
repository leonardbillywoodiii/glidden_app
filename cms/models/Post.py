from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    UserProfile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)

    REQUIRED_FIELDS = [
        'title',
        'body',
        'UserProfile'
    ]

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    UserProfile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = [
        'title',
        'body',
        'UserProfile'
    ]

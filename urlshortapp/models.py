from django.db import models
from django.contrib.auth.models import User

class ShortUrl(models.Model):
    short_url = models.URLField()
    full_url = models.URLField()
    submitter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.short_url

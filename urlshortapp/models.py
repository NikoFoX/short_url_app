from django.db import models

# Create your models here.
class Submitter(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    date_joined = models.DateTimeField()

    def __str__(self):
        return self.username

class ShortUrl(models.Model):
    short_url = models.URLField()
    full_url = models.URLField()
    submitter = models.ForeignKey(Submitter, on_delete=models.CASCADE)

    def __str__(self):
        return self.short_url

from django.db import models
from django.contrib.auth.models import User


class Meeting(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    localization = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    guests = models.ManyToManyField(User, related_name='guests')

    def __str__(self):
        return self.title

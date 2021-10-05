from django.contrib.auth.models import User
from django.db import models


class Availability(models.Model):
    """
    The user can tell us when they are available for the stag
    """
    added_datetime = models.DateTimeField(auto_now_add=True)
    day = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    """
    The user can add comments on the site
    """
    added_datetime = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=140)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

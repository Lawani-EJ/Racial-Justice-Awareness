from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Location(models.Model):
    """A location helps filter which legislation to look at."""

    class Meta:
        app_label = 'fixpol'

    desc = models.CharField(max_length=80)
    shortname = models.CharField(max_length=20)
    hierarchy = models.CharField(max_length=200)
    govlevel = models.CharField(max_length=80)
    parent = models.ForeignKey('self', null=True, 
            related_name='child', on_delete=models.PROTECT)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.desc

class Impact(models.Model):
    """A location helps filter which legislation to look at."""

    class Meta:
        app_label = 'fixpol'

    text = models.CharField(max_length=80)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text







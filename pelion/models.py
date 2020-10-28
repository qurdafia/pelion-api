from django.db import models
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class Attribute(models.Model):
    conf = models.CharField(max_length=200, default="")
    value = models.CharField(max_length=200, default="")
    key = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.conf


class Event(models.Model):
    deviceId = models.CharField(max_length=200)
    deviceName = models.CharField(max_length=200)
    personId = models.CharField(max_length=200)
    personName = models.CharField(max_length=200)
    attributes = models.ForeignKey(Attribute, related_name='attributes', on_delete=models.CASCADE, default="", blank=True)

    def __str__(self):
        return self.deviceName

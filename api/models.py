from django.db import models
from timezone_field import TimeZoneField



# Create your models here.
class User(models.Model):
    real_name = models.TextField()
    tz = TimeZoneField()

class ActivityPeriod(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

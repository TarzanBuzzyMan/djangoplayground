from django.conf import settings
from django.db import models
from django.utils import  timezone

User = settings.AUTH_USER_MODEL

# Create your models here.
class StatusType(models.Model):
    name    = models.CharField(max_length=120)


    def __str__(self):
        display_string = "{}".format(self.name)
        return display_string



class SiteStatusTransaction(models.Model):
    person              = models.ForeignKey(User)
    status_type         = models.ForeignKey(StatusType)
    destination         = models.CharField(max_length=120)
    etd                 = models.DateTimeField(default=timezone.now)
    eta                 = models.DateTimeField()
    arrival_datetime    = models.DateTimeField(blank=True)
    late_meal           = models.BooleanField(default=False)

    def __str__(self):
        display_string = "User: {} Status: {} Destination: {} ETD: {} ETA: {} Arrival {}".format(self.person.username, self.status_type, self.destination, self.etd, self.eta, self.arrival_datetime)
        return display_string
from django.conf import settings
from django.db import models
from django.utils import  timezone

User = settings.AUTH_USER_MODEL

# Create your models here.
class SiteStatusType(models.Model):
    name    = models.CharField(max_length=120)

    def __str__(self):
        display_string = "{}".format(self.name)
        return display_string



class SiteStatus(models.Model):
    persons             = models.ManyToManyField(User)
    site_status_type    = models.ForeignKey(SiteStatusType, on_delete=models.CASCADE)
    destination         = models.CharField(max_length=120)
    etd                 = models.DateTimeField(default=timezone.now)
    eta                 = models.DateTimeField()
    arrival_datetime    = models.DateTimeField(blank=True, null=True)
    late_meal           = models.BooleanField(default=False)

    def __str__(self):
        display_string = "Users: {} Status: {} Destination: {} ETD: {} ETA: {} - Actual Arrival: {}".format(self.get_person_names(), self.site_status_type, self.destination, self.etd, self.eta, self.arrival_datetime)
        return display_string

    def get_person_names(self):
        return ", ".join(person.username for person in self.persons.all())

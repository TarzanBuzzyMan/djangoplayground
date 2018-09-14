from django.contrib import admin
from . import models
# Register your models here.
myModels = [models.SiteStatusType, models.SiteStatus, models.AircraftType, models.Aircraft, models.Booking, models.FlightType, models.FlightAuthorisation]
admin.site.register(myModels)


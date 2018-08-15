from django.contrib import admin
from . import models
# Register your models here.
myModels = [models.SiteStatusType, models.SiteStatus]
admin.site.register(myModels)


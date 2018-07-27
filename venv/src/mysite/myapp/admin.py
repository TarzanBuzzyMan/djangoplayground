from django.contrib import admin
from . import models
# Register your models here.
myModels = [models.StatusType, models.SiteStatusTransaction]
admin.site.register(myModels)


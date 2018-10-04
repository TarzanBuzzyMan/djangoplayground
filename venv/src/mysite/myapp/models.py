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


class AircraftType(models.Model):
    name    = models.CharField(max_length=120)

    def __str__(self):
        display_string = "{}".format(self.name)
        return display_string


class Aircraft(models.Model):
    MAINTENANCE_RECORDED_BY_TACHO = 'T'
    MAINTENANCE_RECORDED_BY_HOBBS = 'H'
    MAINTENANCE_RECORDED_BY_AIRSWITCH = 'A'

    MAINTENANCE_RECORDED_BY_CHOICES = {(MAINTENANCE_RECORDED_BY_TACHO, "Tacho"),
                                       (MAINTENANCE_RECORDED_BY_HOBBS, "Hobbs"),
                                       (MAINTENANCE_RECORDED_BY_AIRSWITCH, "Airswitch")}

    registration                = models.CharField(max_length=10)
    aircraft_type               = models.ForeignKey(AircraftType, on_delete=models.PROTECT)
    maintenance_due             = models.DecimalField(max_digits=10, decimal_places=2)
    maintenance_recorded_by     = models.CharField(max_length=10, choices=MAINTENANCE_RECORDED_BY_CHOICES)
    tacho_time                  = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, blank=True)
    hobbs_time                  = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, blank=True)
    airswitch_time              = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, blank=True)
    serviceable                 = models.BooleanField(default=True)
    notes                       = models.CharField(max_length=120, blank=True)

    def __str__(self):
        serviceable_aircraft = "[UNSERVICEABLE]"
        if self.serviceable:
            serviceable_aircraft = "Serviceable"

        hours_to_run = 0
        if  self.maintenance_recorded_by == Aircraft.MAINTENANCE_RECORDED_BY_TACHO:
            hours_to_run = self.maintenance_due - self.tacho_time
        elif  self.maintenance_recorded_by == Aircraft.MAINTENANCE_RECORDED_BY_HOBBS:
            hours_to_run = self.maintenance_due - self.hobbs_time
        elif self.maintenance_recorded_by == Aircraft.MAINTENANCE_RECORDED_BY_AIRSWITCH:
            hours_to_run = self.maintenance_due - self.airswitch_time


        display_string = "{}-{} {} with {} hours to run".format(self.registration, self.aircraft_type, serviceable_aircraft, hours_to_run)
        return display_string


class Booking(models.Model):
    aircraft            = models.ForeignKey(Aircraft, on_delete=models.CASCADE, blank=True)
    student             = models.ForeignKey(User, related_name='booking_student', blank=True)
    instructor          = models.ForeignKey(User, related_name='booking_instructor', blank=True)
    passengers          = models.ManyToManyField(User,related_name='booking_passengers', blank=True)
    etd                 = models.DateTimeField()
    eta                 = models.DateTimeField()

    def __str__(self):
        display_string = "Aircraft: {} Student: {} Instructor: {} ETD: {} ETA: {}".format(self.aircraft, self.student, self.instructor, self.etd, self.eta)
        return display_string


class FlightType(models.Model):
    FLIGHT_TYPE_SOLO = 'S'
    FLIGHT_TYPE_DUAL = 'D'
    FLIGHT_TYPE_OTHER = 'O'

    FLIGHT_TYPE_CHOICES = {(FLIGHT_TYPE_SOLO, "Solo"),
                           (FLIGHT_TYPE_DUAL, "Dual"),
                           (FLIGHT_TYPE_OTHER, "Other")}

    code                = models.CharField(max_length=10, choices=FLIGHT_TYPE_CHOICES)
    alias               = models.CharField(max_length=120, blank=True, default='')

    def __str__(self):
        display_string = "{}.{}".format(self.get_code_display(), self.alias)
        return display_string


class FlightAuthorisation(models.Model):
    aircraft            = models.ForeignKey(Aircraft, on_delete=models.PROTECT)
    flight_type         = models.ForeignKey(FlightType, on_delete=models.PROTECT)
    student             = models.ForeignKey(User, on_delete=models.PROTECT, related_name='flight_student', blank=True)
    instructor          = models.ForeignKey(User, on_delete=models.PROTECT, related_name='flight_instructor')
    passengers          = models.ManyToManyField(User, related_name='flight_passengers', blank=True)
    etd                 = models.DateTimeField()
    eta                 = models.DateTimeField()
    notes               = models.CharField(max_length=120)
    instructor_signoff  = models.BooleanField(default=False)
    tacho_start         = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tacho_stop          = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    cancelled           = models.BooleanField(default=False)


    def __str__(self):
        signoff = ""
        if not self.instructor_signoff and self.flight_type.code == FlightType.FLIGHT_TYPE_SOLO:
            signoff = "-[NO SIGNOFF]"

        current_status = ""
        if timezone.now() > self.eta:
            if self.flight_time == 0:
                current_status = "[EXPECTED BACK]"
            else:
                current_status = ""
        elif timezone.now() > self.etd:
            current_status = "[Flying]"

        if self.cancelled:
            current_status = "[Cancelled]"

        display_string = "{} {}{} Currently:{} Student:{} Instructor:{} ETD:{} ETA:{}, Notes:{}".format(self.aircraft, self.flight_type, signoff, current_status, self.student, self.instructor, self.etd, self.eta, self.notes)

        return display_string

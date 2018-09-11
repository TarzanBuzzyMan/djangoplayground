from django import forms
from django.utils import timezone
from django.contrib.admin import widgets
from .models import SiteStatus

TIME_CHOICES = (
    (0.0, '00:00'), (0.25,'00:15'), (0.5, '00:30'), (0.75, '00:45'), (1.0, '01:00')
)

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
     input_type = 'time'

class SiteStatusForm(forms.ModelForm):
    etx = forms.ChoiceField(widget=forms.Select(), choices=TIME_CHOICES)
    class Meta:
        model = SiteStatus
        fields = [
            'persons',
            'site_status_type',
            'destination',
            'etd',
            'eta',
            'late_meal',
        ]
        initial = {
            'eta':'00:45',
        }
        widgets = {
            'eta':forms.Select(choices=TIME_CHOICES),
            'etd':forms.SplitDateTimeWidget(attrs={type:'date'}),
        }


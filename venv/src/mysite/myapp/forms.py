from django import forms
from django.utils import timezone
from django.contrib.admin import widgets
from .models import SiteStatus

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
     input_type = 'time'

class SiteStatusForm(forms.ModelForm):
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

        }
        widgets = {
            'eta':widgets.AdminDateWidget(),
            'etd':forms.SplitDateTimeWidget(attrs={type:'date'}),
        }


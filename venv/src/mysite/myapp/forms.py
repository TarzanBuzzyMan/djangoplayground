from django import forms
from .models import SiteStatus


class SiteStatusForm(forms.ModelForm):
    class Meta:
        model = SiteStatus
        fields = [
            'persons',
            'site_status_type',
            'destination',
            'etd',
            'eta',
            'arrival_datetime',
            'late_meal',
        ]

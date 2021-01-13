from django import forms
from .models import Notice


class DatePicker(forms.DateInput):
    input_type = 'datetime-local'


class CreateNoticeForm(forms.ModelForm):

    class Meta:
        model = Notice
        fields = ('title', 'short_description', 'long_description', 'duration',
                  'event_date_time', 'event_location_postcode',
                  'event_location_postcode')

        widgets = {
            'event_date_time': DatePicker()
        }

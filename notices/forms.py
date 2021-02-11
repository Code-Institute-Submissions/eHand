from django import forms
from .models import Notice


class DatePicker(forms.DateInput):
    input_type = 'date'


class CreateNoticeForm(forms.ModelForm):

    class Meta:
        model = Notice
        fields = ('title', 'short_description', 'long_description', 'duration',
                  'event_date', 'event_location_postcode')

        widgets = {
            'event_date': DatePicker()
        }

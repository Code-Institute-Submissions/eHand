from django import forms
from .models import Notice


class DateInput(forms.DateInput):
    input_type = 'date'


class CreateNoticeForm(forms.ModelForm):

    class Meta:
        model = Notice
        fields = ('title', 'short_description', 'long_description', 'duration',
                  'specify_date', 'event_location_postcode')
        widgets = {
            'specify_date': DateInput(),
        }


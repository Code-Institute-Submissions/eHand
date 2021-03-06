from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """ Creates a form with custom placeholders for the profile

    CREDIT: Code Institute - dont think any improvement
    is needed or possible on this code, for my needs - thank you.
    """
    class Meta:
        model = UserProfile
        exclude = ('user', 'time_balance')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """

        super().__init__(*args, **kwargs)

        # create a dictionary of placeholders and match them to fields from
        # model
        placeholders = {

            'full_name': 'Full Name',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder

            self.fields[field].widget.attrs['class'] = ('border-black '
                                                        'rounded-0 '
                                                        'profile-form-input')
            self.fields[field].label = False

        # autofocus on default phone number
        self.fields['full_name'].widget.attrs['autofocus'] = True

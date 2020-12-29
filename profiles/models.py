from django.db import models
from django.contrib.auth.models import User

from django_countries.fields import CountryField


TIME_OPTIONS = {
    ('Not Specified', '0'),
    ('1 Hour', '1'),
    ('2 Hours', '2'),
    ('3 Hours', '3'),
    ('4 Hours', '4'),
    ('5 Hours', '5'),
    ('6 Hours', '6'),
    ('7 Hours', '7'),
    ('8 Hours', '8')
}

class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    personal information including Time Balance
    """
    # only one profile for each user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    time_balance = models.DecimalField(
        choices=TIME_OPTIONS,
        max_length=40,
        default='Not Specified')
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=True, blank=True)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    default_country = CountryField(blank_label="Country", blank=True, null=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.username

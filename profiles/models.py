from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    personal information including Time Balance
    """
    # only one profile for each user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Setting a default of -1 as we want to check for this initial state when
    # creating memberships. -1 will be an inactive state
    time_balance = models.IntegerField(null=True, blank=True, default=-1)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=True, blank=True)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    default_country = CountryField(blank_label="Country", blank=True, null=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    A receiver for the post save event from the user model.
    Creates/ updates profile

    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()

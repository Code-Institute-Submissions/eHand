from django.conf import settings
from django.db import models

PACKAGE_OPTIONS = {
    ('Premium', 'prem'),
    ('Free', 'free')
}


class Packages(models.Model):
    slug = models.SlugField()
    package_type = models.CharField(
        choices=PACKAGE_OPTIONS,
        max_length=40,
        default='Free')
    package_price = models.IntegerField(default=5)
    stripe_plan_id = models.CharField(max_length=50)

    def __str__(self):
        return self.package_type


class Memberships(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_user_id = models.CharField(max_length=50)
    membership_type = models.ForeignKey(
        Packages, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username


class Subscriptions(models.Model):
    user_membership = models.ForeignKey(Memberships, on_delete=models.CASCADE)
    valid = models.BooleanField(default=True)
    stripe_sub_id = models.CharField(max_length=50)

    def __str__(self):
        return self.user_membership.user.username

from django.conf import settings
from django.db.models.signals import post_save
from django.db import models
from datetime import datetime

import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

PACKAGE_OPTIONS = {
    ('Premium', 'prem'),
    ('Free', 'free')
}


class Packages(models.Model):

    class Meta:
        verbose_name_plural = 'Packages'

    package_type = models.CharField(
        choices=PACKAGE_OPTIONS,
        max_length=40,
        default='Free')
    package_price = models.IntegerField(default=5)
    stripe_plan_id = models.CharField(max_length=50)

    def __str__(self):
        return self.package_type


class Memberships(models.Model):

    class Meta:
        verbose_name_plural = 'Memberships'

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_user_id = models.CharField(max_length=50)
    membership_type = models.ForeignKey(
        Packages, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username


def post_save_create_memberships(sender, instance, created, *args, **kwargs):
    if created:
        Memberships.objects.get_or_create(user=instance)

    membership, created = Memberships.objects.get_or_create(user=instance)

    # check if there is currently a stripe
    # customer id
    if membership.stripe_user_id is None or membership.stripe_user_id == '':
        # create the customer object on stripe
        new_customer_id = stripe.Customer.create(email=instance.email)
        free = Packages.objects.get(package_type='Free')
        membership.stripe_user_id = new_customer_id['id']
        membership.membership_type = free
        membership.save()


# unable to call signal from signals file so called from here
# using post_save
post_save.connect(post_save_create_memberships,
                  sender=settings.AUTH_USER_MODEL)


class Subscriptions(models.Model):

    class Meta:
        verbose_name_plural = 'Subscriptions'

    user_membership = models.ForeignKey(Memberships, on_delete=models.CASCADE)
    valid = models.BooleanField(default=False)
    stripe_sub_id = models.CharField(max_length=50)

    def __str__(self):
        return self.user_membership.user.username

    @property
    def get_created_date(self):
        """ Get the subscription model from the stripe database
            Then get the created date from there. """
        # from stripe docs
        subscription = stripe.Subscription.retrieve(
            self.stripe_sub_id)
        # return converted timestamp using datetime
        return datetime.fromtimestamp(subscription.created)

    @property
    def get_next_payment_date(self):
        """ Get the subscription model from the stripe database
            Then get the next payment date. """

        # from stripe docs
        subscription = stripe.Subscription.retrieve(
            self.stripe_sub_id)
        # return the converted timestamp
        return datetime.fromtimestamp(subscription.current_period_end)

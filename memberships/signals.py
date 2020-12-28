# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from .models import Memberships
# from django.dispatch import receiver

# import stripe


# @receiver(post_save, sender=User)
# def post_save_create_memberships(sender, instance, created, **kwargs):
#     if created:
#         Memberships.objects.get_or_create(user=instance)

#     membership, created = Memberships.objects.get_or_create(user=instance)

#     # check if there is currently a stripe
#     # customer id
#     if (membership.stripe_customer_id is None or
#             membership.stripe_customer_id == ''):
#         # create the customer object on stripe
#         new_customer_id = stripe.Customer.create(email=instance.email)
#         # grab the id from that object
#         membership.stripe_customer_id = new_customer_id['id']
#         membership.save()

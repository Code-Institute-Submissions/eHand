from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from profiles.models import UserProfile
from .models import Packages, Memberships, Subscriptions

import stripe

# Create your views here.


def get_current_package(request):
    """ A helper funtion that retrieves the membership package that the user
    is currently subscribed to.
    """

    current = get_object_or_404(Memberships, user=request.user)
    if current:
        return current
    return None


def get_user_subscription(request):
    """ A helper funtion that retrieves the users current subscription
    """

    # look in subscriptions for the current user
    query_subscription = Subscriptions.objects.filter(
        user_membership=get_current_package(request))
    if query_subscription.exists():
        user_subscription = query_subscription.first()
        return user_subscription


def get_selected_package(request):
    """ A helper funtion that gets the selected package from session storage
    """
    package_type = request.session['selected_package_type']
    # convert it to an object

    selected_package_query = get_object_or_404(
            Packages, package_type=package_type)
    if selected_package_query:
        return selected_package_query
    return None


@login_required
def select_package(request):
    """ A view that returns the membership selection page """

    packages = Packages.objects.all()
    # Get the users current package - we want to compare this in the template
    # Also needed in post section
    current_package = get_current_package(request)

    if request.method == 'POST':
        # Get the posted info - then gets it in object form
        selected_package_type = request.POST.get('package_type')
        selected_package_query = get_object_or_404(
            Packages, package_type=selected_package_type)
        if selected_package_query:
            selected_package = selected_package_query

        # Get the current users subscription
        user_subscription = get_user_subscription(request)

        # check if current = selected - this should not be possible
        # but need to let them know they already have this package
        if current_package.membership_type == selected_package:
            if user_subscription is not None:
                messages.info(request, "This is your existing membership package. \
                    Your next payment is due on: {}".format(
                        'need to get this from stripe'))
                # send user back to the page they came -  packages
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        # Now we can save the selected_package into session storage
        # because we want to pass it to the next view
        request.session[
            'selected_package_type'] = selected_package.package_type
        return HttpResponseRedirect(reverse('payment'))

    context = {
        'packages': packages,
        'current_package': str(current_package.membership_type)
    }
    return render(request, 'memberships/select_package.html', context)


def package_payment(request):
    """ Get the stripe payment form for the user
        Also handle the payment

    * Stripe subscription source:
    https://stripe.com/docs/api/subscriptions/create?lang=python
    """
    # get some required variables
    current_package = get_current_package(request)
    selected_package = get_selected_package(request)
    public_key = settings.STRIPE_PUBLIC_KEY

    if request.method == "POST":
        try:
            # add the token
            token = request.POST['stripeToken']

            # We must add the source for the customer
            customer = stripe.Customer.retrieve(current_package.stripe_user_id)
            customer.source = token
            customer.save()

            # Now we can create the subscription using only the customer,
            # we don't need to pass their credit card source(token)
            # subscription = the intent
            subscription = stripe.Subscription.create(
                customer=current_package.stripe_user_id,
                items=[
                    {"price": selected_package.stripe_plan_id}
                ]
            )

            # pass the subscription id into the upgraded-transactions view
            return redirect(reverse("upgradedtransactions",
                                    kwargs={'subscription_id':
                                            subscription.id}))

        except stripe.error.CardError as e:
            messages.info(request, f"{e.code} - Your card has ben declined")

    context = {
        'selected_package': selected_package,
        'public_key': public_key
    }
    return render(request, "memberships/package_payment.html", context)


def upgradedtransactions(request, subscription_id):
    """ Handles upgrading of membership models and
    returning success message """

    # get some required variables
    current_package = get_current_package(request)
    selected_package = get_selected_package(request)

    # so now we can set the current package as the chosen package, which is
    # the one they just paid for
    current_package.membership_type = selected_package
    current_package.save()

    # create or update subscription - check if created
    subscription, created = Subscriptions.objects.get_or_create(
        user_membership=current_package)
    subscription.stripe_sub_id = subscription_id  # passed in
    subscription.valid = True
    subscription.save()

    # Set the users Time Balance back to 10 free hours - one off
    profile = get_object_or_404(UserProfile, user=request.user)
    profile.time_balance = 10
    profile.save()

    # remove session storage
    try:
        del request.session['selected_package_type']
    except request.session['selected_package_type'].DoesNotExist:
        pass

    messages.success(request, f"You have been successfully upgraded to our \
         {selected_package} membership")

    return redirect('profile')


@login_required
def cancel_user_subscription(request):
    """ View to handle the cancelling of a users subscription """
    current_user_subscription = get_user_subscription(request)

    # If the user does not have a subscription then return with a message
    if current_user_subscription.valid is False:
        messages.warning(request, "You dont have an active membership")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    # get the subscription from stripe - then delete it.
    subscription = stripe.Subscription.retrieve(
        current_user_subscription.stripe_sub_id)
    subscription.delete()

    # set the subscrption database subscription info accordingly
    current_user_subscription.valid = False
    current_user_subscription.save()

    # Get free membership and get current package user is on
    # Then set curren package for user as free.
    free = Packages.objects.get(package_type='Free')
    user_package = get_current_package(request)
    user_package.membership_type = free
    user_package.save()

    # Set the users Time Balance back to -1
    profile = get_object_or_404(UserProfile, user=request.user)
    profile.time_balance = -1
    profile.save()

    messages.success(
        request, "You have successfully \
            cancelled your subscription to Premium.")

    return redirect(reverse('profile'))

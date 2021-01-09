from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
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

        # Validate

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
            print(f"################################################# {token}")

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
            print(f"SUBSCRIPTION  ################################################# {subscription.id}")
            # pass the subscription id into the upgraded-transactions view
            return redirect(reverse("upgradedtransactions",
                                    kwargs={'subscription_id': subscription.id}))

        except stripe.error.CardError as e:
            messages.info(request, f"{e.code} - Your card has ben declined")

    context = {
        'selected_package': selected_package,
        'public_key': public_key
    }
    return render(request, "memberships/package_payment.html", context)


def upgradedtransactions(request, subscription_id):
    """ return a template for upgraded subscriptions """

    # get some required variables
    current_package = get_current_package(request)
    selected_package = get_selected_package(request)

    # so now we can set the current package as the chosen package, which is
    # the one they just paid for
    current_package.membership_type = selected_package
    current_package.save()

    # create or update subscription
    subscription, created = Subscriptions.objects.get_or_create(
        user_membership=current_package)
    subscription.stripe_sub_id = subscription_id  # passed in
    subscription.valid = True
    subscription.save()

    # remove session storage
    try:
        del request.session['selected_package_type']
    except:
        pass

    messages.success(request, f"You have been successfully upgraded to our \
         {selected_package} membership")

    return redirect('home')

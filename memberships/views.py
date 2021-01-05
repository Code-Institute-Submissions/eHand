from django.shortcuts import render, get_object_or_404
from .models import Packages, Memberships, Subscriptions
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


def select_package(request):
    """ A view that returns the membership selection page """

    packages = Packages.objects.all()
    # Get the users current package - we want to compare this in the template
    # Also needed in post section
    current_package = get_current_package(request)

    if request.method == 'POST':
        # Get the posted info
        selected_package_type = request.POST.get('package_type')
        # Get the current users subscription
        user_subscription = get_user_subscription(request)

        # check if the users current package is same as selected
        selected_package_query = get_object_or_404(
            Packages, package_type=selected_package_type)
        if selected_package_query:
            selected_package = selected_package_query

        print(f"#################### selected package ------- {selected_package}")
        print(f"#################### user subscrip ------- {user_subscription}")


    context = {
        'packages': packages,
        'current_package': str(current_package.membership_type)
    }
    return render(request, 'memberships/select_package.html', context)

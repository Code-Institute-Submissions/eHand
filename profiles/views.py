from django.shortcuts import render
from memberships.views import get_current_package, get_user_subscription


def profile_view(request):
    """ A view to handle displaying of profile """

    current_package = get_current_package(request)
    user_subscription = get_user_subscription(request)

    context = {
        'users_current_package': current_package,
        'users_current_subscription': user_subscription
    }
    return render(request, 'profiles/profile.html', context)

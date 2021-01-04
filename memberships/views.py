from django.shortcuts import render, get_object_or_404
from .models import Packages, Memberships
# Create your views here.


def get_current_package(request):
    """ A helper funtion that retrieves the membership package that the user
    is currently subscribed to.
    """
    current = get_object_or_404(Memberships, user=request.user)
    return str(current.membership_type)


def select_package(request):
    """ A view that returns the membership selection page """

    packages = Packages.objects.all()
    current_package = get_current_package(request)
    context = {
        'packages': packages,
        'current_package': current_package
    }
    return render(request, 'memberships/select_package.html', context)

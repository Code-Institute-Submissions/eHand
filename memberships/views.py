from django.shortcuts import render
from .models import Packages
# Create your views here.


def select_package(request):
    """ A view that returns the membership selection page """

    packages = Packages.objects.all()
    context = {
        'packages': packages
    }
    return render(request, 'memberships/select_package.html', context)

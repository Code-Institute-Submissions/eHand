from django.shortcuts import render
from django.conf import settings


# Create your views here.
def index(request):
    """ A view that returns the home page """

    debug_flag = settings.DEBUG
    context = {'debug_flag': debug_flag}

    return render(request, 'home/index.html', context)

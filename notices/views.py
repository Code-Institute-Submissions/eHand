from django.shortcuts import render, get_object_or_404
from .models import Notice


def notices(request):
    """ A view that returns the notices page """

    context = {
        'notices': Notice.objects.all()
    }

    return render(request, 'notices/notice_board.html', context)


def notice_details(request, notice_id):
    """ A view that returns the notice details page """

    notice = get_object_or_404(Notice, pk=notice_id)

    context = {
        'notice': notice
    }

    return render(request, 'notices/notice_details.html', context)

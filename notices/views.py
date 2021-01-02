from django.shortcuts import render

def notices(request):
    """ A view that returns the notices page """

    return render(request, 'notices/notice_board.html')
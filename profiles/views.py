from django.shortcuts import render, get_object_or_404
from memberships.views import get_current_package, get_user_subscription
from django.contrib.auth.models import User
from django.views.generic import (
    ListView
)
from notices.models import Notice
from .models import UserProfile


def profile_view(request):
    """ A view to handle displaying of profile """

    current_package = get_current_package(request)
    user_subscription = get_user_subscription(request)
    profile = get_object_or_404(UserProfile, user=request.user)

    context = {
        'users_current_package': current_package,
        'users_current_subscription': user_subscription,
        'profile': profile
    }
    return render(request, 'profiles/profile.html', context)


class CommitmentsListView(ListView):
    """ Returns as a view the notices commited to by logged in user """
    model = Notice
    template_name = 'profiles/member_commitments.html'
    paginate_by = 2

    def get_queryset(self):
        user = self.request.user
        return Notice.objects.filter(commit=user).order_by('-date_posted')


class MemberNoticesListView(ListView):
    """ Returns as a view the logged in users Notices """
    model = Notice
    template_name = 'profiles/member_notices.html'
    paginate_by = 2

    def get_queryset(self):
        user = self.request.user
        return Notice.objects.filter(author=user).order_by('-date_posted')

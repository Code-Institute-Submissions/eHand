from django.shortcuts import render, get_object_or_404
from memberships.views import get_current_package, get_user_subscription
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    UpdateView
)
from notices.models import Notice
from .models import UserProfile
from .forms import UserProfileForm

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)


@login_required
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


class CommitmentsListView(LoginRequiredMixin, ListView):
    """ Returns as a view the notices commited to by logged in user """
    model = Notice
    template_name = 'profiles/member_commitments.html'
    paginate_by = 2

    def get_queryset(self):
        user = self.request.user
        return Notice.objects.filter(commit=user).order_by('-date_posted')


class MemberNoticesListView(LoginRequiredMixin, ListView):
    """ Returns as a view the logged in users Notices """
    model = Notice
    template_name = 'profiles/member_notices.html'
    paginate_by = 2

    def get_queryset(self):
        user = self.request.user
        return Notice.objects.filter(author=user).order_by('-date_posted')


class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Returns as a view the profile_form template
        To edit a users profile
    """
    model = UserProfile
    form_class = UserProfileForm
    success_url = '/profile/'

    def form_valid(self, form):
        """ To set correct instance of the form """
        form.instance.profile = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """ test function - ran by UserPassesTestMixin to check condition
            condition check: Is user attempting to update profile equal
            to the current user
        """
        profile_id = self.get_object().id
        if self.request.user.id == profile_id:
            # then we can allow updating
            return True
        return False

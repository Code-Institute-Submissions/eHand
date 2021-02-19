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
    """ A view to handle displaying of profile

    \n * Provide context to the profile page:
    \n   *  current_package
    \n   *  user_subscription
    \n   *  profile


    \nArgs:
    \n * Arg1: The request object.

    \nReturns:
    \n * Redirects to the profiles/profile.html page
    """

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
    """ Returns as a view the notices commited to by the current user

    \nArgs:
    \n * Arg1: The LoginRequiredMixin
    \n * Arg2: Inherits the Generic ListView class.

    \nReturns:
    \n * Returns the profiles/member_commitments.html Template.
    """
    model = Notice
    template_name = 'profiles/member_commitments.html'
    paginate_by = 2

    def get_queryset(self):
        """
        Adjust the order of the Notices
        """
        user = self.request.user
        return Notice.objects.filter(commit=user).order_by('-date_posted')


class MemberNoticesListView(LoginRequiredMixin, ListView):
    """ Returns as a view the logged in users Notices

    \nArgs:
    \n * Arg1: The LoginRequiredMixin
    \n * Arg2: Inherits the Generic ListView class.

    \nReturns:
    \n * Returns the profiles/member_notices.html Template.
    """
    model = Notice
    template_name = 'profiles/member_notices.html'
    paginate_by = 2

    def get_queryset(self):
        """ Adjusts the order of the notices. """
        user = self.request.user
        return Notice.objects.filter(author=user).order_by('-date_posted')


class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Returns as a view the profile_form template
        To edit a users profile

    \nArgs:
    \n * Arg1: The LoginRequiredMixin
    \n * Arg2: The UserPassesTestMixin
    \n * Arg3: Inherits the Generic UpdateView class.

    \nReturns:
    \n * Returns the userprofile_form Template.
    \n * If Success: Returns the /profile/ URL.
    """
    model = UserProfile
    form_class = UserProfileForm
    success_url = '/profile/'

    def form_valid(self, form):
        """ Set the correct instance of the form """
        form.instance.profile = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """ Check user attempting to update profile equal
            to the current user

        \nArgs:
        \n * Arg1: Self - the current instance of the class

        \nReturns:
        \n * True if user is current user, else False
        """
        profile_id = self.get_object().id
        if self.request.user.id == profile_id:
            # then we can allow updating
            return True
        return False

from django.shortcuts import reverse, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Notice
from memberships.models import Memberships
from comments.models import Comment
from profiles.models import UserProfile
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.contrib.auth.models import User
from .forms import CreateNoticeForm
from comments.forms import CommentForm


def accept_notice(request, pk):
    """ view to handle a user clicking to commit to a Notice
    Sets the commit field to logged in user -
    We then use a search to pull the notice into the users profile  """
    notice = get_object_or_404(
        Notice, id=request.POST.get('notice_id'))
    notice.commit = request.user
    notice.save()
    author = str(notice.author).capitalize()
    acceptee = str(notice.commit).capitalize()
    messages.success(request, f"Thank you {acceptee}. You have accepted to provide \
        help to {author}. ")

    return redirect('/profile/member_commitments/')


def cancel_notice(request, pk):
    """ View to handle cancelling of a commitment to a Notice """
    notice = get_object_or_404(
        Notice, id=request.POST.get('notice_id'))
    acceptee = str(notice.commit).capitalize()
    admin = User.objects.get(username='admin')
    notice.commit = admin
    notice.save()
    author = str(notice.author).capitalize()
    messages.success(request, f"{acceptee}, you have successfully cancelled your \
        commitment to {author}'s {notice.title} Notice' ")

    return redirect('/profile/member_commitments/')


def time_transfer(request, notice):
    """ Method to handle the transfer of
        Time from one acc to the other
    """
    admin = User.objects.get(username='admin')

    # First check if acceptee has a premium account
    duration = notice.duration
    time_amt_string = ''.join([i for i in duration if i.isdigit()])
    notice_time_amt = int(time_amt_string)

    # Get the Time Balance of the author
    author = get_object_or_404(UserProfile, user=notice.author.id)
    author_time_balance = author.time_balance

    # Get the Time Balance of the acceptee
    acceptee_profile = get_object_or_404(
        UserProfile, user=notice.commit.id)
    acceptee_time_balance = author_time_balance

    # Transfer the Time amount - check current credit
    if author_time_balance <= 0:
        messages.error(request, "You are unable to complete this transaction \
            as you have 0 funds in your Time acc")
        return redirect('profile')
    elif author_time_balance > 0 and author_time_balance < notice_time_amt:
        messages.error(request, "You are unable to complete this transaction \
            as you insufficient funds in your Time acc")
        return redirect('profile')
    elif author_time_balance >= notice_time_amt:
        author_time_balance -= notice_time_amt
        author.time_balance = author_time_balance
        author.save()
        acceptee_time_balance += notice_time_amt
        acceptee_profile.time_balance = acceptee_time_balance
        acceptee_profile.save()
        notice.commit = admin
        notice.save()
    else:
        # Some error has  occured
        messages.error(request, "Apologies but we are unable to complete \
            this transaction at present. Please check required amounts \
                and your own Time Acc blance and try again later.")
        return redirect('profile')


def complete_notice(request, pk):
    """
    \n* Checks if user is notice author
    \n* Calls time_transfer to handle payment
    \n* Remove Acceptee the acceptee in notice.commit
    \n* Give option to delete Notice
    """

    # check if user is author
    notice = get_object_or_404(
        Notice, id=pk)
    if request.user == notice.author:

        # Check acceptee's membership type
        acceptee_membership = get_object_or_404(
            Memberships, user=notice.commit.id)
        acceptee_membership_type = str(
            acceptee_membership.membership_type).lower()

        # Handle free - remove from notice ONLY
        if acceptee_membership_type == 'free':
            acceptee = notice.commit
            admin = User.objects.get(username='admin')
            notice.commit = admin
            notice.save()

            # Then pass them onto option to delete notice
            messages.success(request, "The Notice has been completed - No \
                transfer of Time was required as {acceptee} is not a \
                    Premium Membership")
            return HttpResponseRedirect(reverse(
                "notices:notice-delete", kwargs={'pk': pk}))

        elif acceptee_membership_type == 'premium':
            duration = notice.duration
            time_amt_string = ''.join([i for i in duration if i.isdigit()])
            notice_time_amt = int(time_amt_string)
            acceptee = notice.commit
            time_transfer(request, notice)
            messages.success(request, f"The Notice has been completed - You \
                have sent {notice_time_amt}hrs of TIME to {acceptee}")
            return HttpResponseRedirect(reverse(
                "notices:notice-delete", kwargs={'pk': pk}))
    else:
        messages.warning(request, "You are not allowed to finalise another\
            members notice")
        return redirect('profile')


class NoticeListView(ListView):
    """ Returns as a view the notice template """
    model = Notice
    ordering = ['-date_posted']
    paginate_by = 2

    def get_context_data(self, **kwargs):
        """
        Include the current Membership of the user in the context

        * Must account for users who are not logged in

        """
        context = super(NoticeListView, self).get_context_data(**kwargs)
        context['membership'] = False
        if self.request.user.is_authenticated:
            req_context = get_object_or_404(
                Memberships, user=self.request.user)
            context['membership'] = str(req_context.membership_type).lower()
        return context


class NoticeDetailView(LoginRequiredMixin, DetailView):
    """ Returns as a view the notice details template """

    model = Notice

    def get_context_data(self, **kwargs):
        """ Getting the context of detailView and add the form to it """
        context = super(NoticeDetailView, self).get_context_data(**kwargs)
        form = CommentForm()
        context['form'] = form
        return context


class CreateComment(CreateView):
    """ Handles actually creating a comment """
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse(
            'notices:notice-detail', kwargs={'pk': self.object.notice.pk})

    def form_valid(self, form):
        """ overrides form_valid to set the user
         making the comment.
         Also sets the notice id before validating form"""

        form.instance.user = self.request.user
        return super().form_valid(form)


class NoticeCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """ Returns as a view the create a notice template """
    model = Notice
    form_class = CreateNoticeForm

    def form_valid(self, form):
        """ overrides form_valid to set the author before validating form"""

        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """ test function - ran by UserPassesTestMixin to check condition
            condition check:
            \n Does the user have a Premium membership
        """
        users_membership = get_object_or_404(
            Memberships, user=self.request.user)
        users_membership_type = str(
            users_membership.membership_type).lower()

        if users_membership_type == 'premium':
            # then we can allow updating creation of notice
            return True
        return False


class NoticeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Returns as a view the create a notice template """
    model = Notice
    fields = ['title', 'short_description', 'long_description', 'duration',
              'event_date_time', 'event_location_postcode',
              'event_location_postcode']

    # override form_valid
    def form_valid(self, form):
        # set the author
        form.instance.author = self.request.user
        # then validate form
        return super().form_valid(form)

    def test_func(self):
        """ test function - ran by UserPassesTestMixin to check condition
            condition check: Is user attempting to update notice equal
            to the author of the notice
        """
        notice = self.get_object()
        if self.request.user == notice.author:
            # then we can allow updating
            return True
        return False


class NoticeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Handles deletion of a Notice """
    model = Notice
    success_url = '/profile/member_notices'

    def test_func(self):
        """ test function - ran by UserPassesTestMixin to check condition
            condition check: Is user attempting to Delete a notice equal
            to the author of the notice
        """
        notice = self.get_object()
        if self.request.user == notice.author:
            # then we can allow updating
            return True
        messages.warning(self.request, "You are not allowed to Delete another \
            members Notice")
        return False



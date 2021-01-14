from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib import messages
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from .forms import CreateNoticeForm
from .models import Notice


def accept_notice(request, pk):
    notice = get_object_or_404(
        Notice, id=request.POST.get('notice_id'))
    notice.commit = request.user
    notice.save()
    author = str(notice.author).capitalize()
    acceptee = str(notice.commit).capitalize()
    messages.success(request, f"Thank you {acceptee}. You have accepted to provide \
        help to {author}. ")

    return redirect('/profile')


class NoticeListView(ListView):
    """ Returns as a view the notice template """
    model = Notice
    ordering = ['-date_posted']
    paginate_by = 2


class NoticeDetailView(DetailView):
    """ Returns as a view the notice details template """
    model = Notice


class NoticeCreateView(LoginRequiredMixin, CreateView):
    """ Returns as a view the create a notice template """
    model = Notice
    form_class = CreateNoticeForm
    # fields = ['title', 'short_description', 'long_description', 'duration',
    #           'event_date_time', 'event_location_postcode',
    #           'event_location_postcode']

    def form_valid(self, form):
        """ overrides form_valid to set the author before validating form"""

        form.instance.author = self.request.user
        return super().form_valid(form)


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
    success_url = '/notices'

    def test_func(self):
        """ test function - ran by UserPassesTestMixin to check condition
            condition check: Is user attempting to Delete a notice equal
            to the author of the notice
        """
        notice = self.get_object()
        if self.request.user == notice.author:
            # then we can allow updating
            return True
        messages.warning(self.request, "You are not allowed to Delete another members Notice")
        return False



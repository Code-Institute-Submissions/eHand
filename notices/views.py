from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Notice


class NoticeListView(ListView):
    """ Returns as a view the notice template """
    model = Notice
    ordering = ['-date_posted']


class NoticeDetailView(DetailView):
    """ Returns as a view the notice details template """
    model = Notice


class NoticeCreateView(LoginRequiredMixin, CreateView):
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


class NoticeUpdateView(LoginRequiredMixin, UpdateView):
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
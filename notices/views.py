from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Notice


class NoticeListView(ListView):
    """ Returns as a view the notice template """
    model = Notice
    ordering = ['-date_posted']


class NoticeDetailView(DetailView):
    """ Returns as a view the notice details template """
    model = Notice


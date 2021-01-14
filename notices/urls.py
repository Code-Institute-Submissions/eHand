from django.urls import path
from .views import (
    NoticeListView,
    NoticeDetailView,
    NoticeCreateView,
    NoticeUpdateView,
    NoticeDeleteView
)

from . import views


urlpatterns = [
    path('',
         NoticeListView.as_view(),
         name='notice-list'),
    path('notice/<int:pk>/',
         NoticeDetailView.as_view(),
         name='notice-detail'),
    path('notice/create/',
         NoticeCreateView.as_view(),
         name='notice-create'),
    path('notice/<int:pk>/update/',
         NoticeUpdateView.as_view(),
         name='notice-update'),
    path('notice/<int:pk>/delete/',
         NoticeDeleteView.as_view(),
         name='notice-delete'),
    path('accept/<int:pk>/',
         views.accept_notice,
         name='accept-notice'),
]

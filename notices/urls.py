from django.urls import path
from .views import NoticeListView, NoticeDetailView
from . import views


urlpatterns = [
    path('', NoticeListView.as_view(), name='notice-list'),
    path('notice/<int:pk>/', NoticeDetailView.as_view(), name='notice-detail'),
]

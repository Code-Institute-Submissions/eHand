from django.urls import path
from profiles import views
from .views import (
    CommitmentsListView
)


urlpatterns = [
    path('', views.profile_view, name='profile'),
    path('member_commitments/',
         CommitmentsListView.as_view(),
         name='member-commitments'),
]

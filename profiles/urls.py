from django.urls import path
from profiles import views
from .views import (
    CommitmentsListView,
    MemberNoticesListView,
    ProfileUpdateView
)


urlpatterns = [
    path('', views.profile_view, name='profile'),
    path('member_commitments/',
         CommitmentsListView.as_view(),
         name='member-commitments'),
    path('member_notices/',
         MemberNoticesListView.as_view(),
         name='member-notices'),
    path('profile/<int:pk>/update/',
         ProfileUpdateView.as_view(),
         name='profile-update'),
]

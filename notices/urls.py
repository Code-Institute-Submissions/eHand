from django.urls import path
from . import views


urlpatterns = [
    path('', views.notices, name='notices'),
    path('<int:notice_id>/', views.notice_details, name='notice_details'),
]

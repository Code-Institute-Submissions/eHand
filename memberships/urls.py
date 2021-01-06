from django.urls import path
from . import views


urlpatterns = [
    path('', views.select_package, name='packages'),
    path('payment', views.package_payment, name='payment'),

]

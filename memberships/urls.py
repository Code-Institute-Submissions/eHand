from django.urls import path
from . import views


urlpatterns = [
    path('', views.select_package, name='packages'),
    path('payment/', views.package_payment, name='payment'),
    path('upgradedtransactions/<subscription_id>/',
         views.upgradedtransactions,
         name='upgradedtransactions'),
    path('cancel_sub/', views.cancel_user_subscription, name='cancel_sub'),


]

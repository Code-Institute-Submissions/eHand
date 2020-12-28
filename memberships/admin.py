from django.contrib import admin

from .models import Packages, Memberships, Subscriptions

admin.site.register(Packages)
admin.site.register(Memberships)
admin.site.register(Subscriptions)

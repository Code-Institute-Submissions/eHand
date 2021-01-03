from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Allauth
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('notices/', include('notices.urls')),
    path('packages/', include('memberships.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

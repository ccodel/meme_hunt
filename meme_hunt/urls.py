"""
meme_hunt URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django built-in admin
    path('admin/', admin.site.urls),

    # User management
    path('accounts/', include('allauth.urls')),

    # Local apps
    path('', include('pages.urls')),
]

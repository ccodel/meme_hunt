"""
meme_hunt URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Django built-in admin
    path('admin/', admin.site.urls),

    # User management
    path('accounts/', include('allauth.urls')),

    # Local apps
    path('', include('pages.urls')),
    path('memes/', include('memes.urls')),
    path('scoreboard/', include('scoreboard.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # TODO prod

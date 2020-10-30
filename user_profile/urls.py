from django.urls import path

from .views import *

urlpatterns = [
    path('', UserProfileView.as_view(), name='profile'),
    path('user_profiles', UserProfileListView.as_view(), name='profile_list'),
]

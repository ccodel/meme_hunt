from django.urls import path

from .views import *

urlpatterns = [
    path('', ScoreboardView.as_view(), name='scoreboard'),
]

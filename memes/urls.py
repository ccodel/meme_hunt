from django.urls import path

from .views import *

urlpatterns = [
    path('', MemeListView.as_view(), name='meme_list'),
    path('<uuid:pk>', MemeDetailView.as_view(), name='meme_detail'),
    path('create_meme/', MemeCreationView.as_view(), name='meme_creation'),
    path('locate/<uuid:secret_key>', MemeLocateView.as_view(), name='meme_locate'),
]

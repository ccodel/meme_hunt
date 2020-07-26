from django.urls import path

from .views import MemeListView, MemeDetailView

urlpatterns = [
    path('', MemeListView.as_view(), name='meme_list'),
    path('<uuid:pk>', MemeDetailView.as_view(), name='meme_detail'),
]

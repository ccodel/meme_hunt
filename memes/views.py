from django.views.generic import ListView, DetailView

from .models import Meme


class MemeListView(ListView):
    model = Meme
    context_object_name = 'meme_list'
    template_name = 'memes/meme_list.html'


class MemeDetailView(DetailView):
    model = Meme
    context_object_name = 'meme'
    template_name = 'memes/meme_detail.html'

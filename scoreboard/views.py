from django.contrib import messages
from django.shortcuts import render
from django.views.generic import ListView

from .models import Find
from memes.models import Meme

class ScoreboardView(ListView):
    model = Find
    context_object_name = 'find_list'
    template_name = 'scoreboard/scoreboard.html'

    def get(self, request):
        find_list = Find.objects.all().order_by('-score')
        meme = Meme.latest()
        # TODO filter out by time?
        return render(request, self.template_name, 
                {'find_list': find_list, 'meme': meme})

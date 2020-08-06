from django.views.generic import TemplateView
from django.shortcuts import render
from django.urls import reverse

from memes.models import Meme

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        meme = Meme.latest()
        return render(request, self.template_name, {'meme': meme})

class AboutPageView(TemplateView):
    template_name = 'about.html'

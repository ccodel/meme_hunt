from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from .models import Meme
from .forms import MemeForm

def create_meme(request):
    if request.method == 'POST':
        # Create a new form instance
        form = MemeForm(request.POST)
        if form.is_valid():
            messages.add_message(request, messages.INFO, 'Meme created successfully.')
            return HttpResponseRedirect('/create_meme/')
    else:
        form = MemeForm()

    return render(request, 'memes/meme_creation.html', {'form': form})

class MemeListView(ListView):
    model = Meme
    context_object_name = 'meme_list'
    template_name = 'memes/meme_list.html'

    def get(self, request):
        meme_list = Meme.objects.all()
        return render(request, self.template_name, {'meme_list': meme_list})


class MemeDetailView(DetailView):
    model = Meme
    context_object_name = 'meme'
    template_name = 'memes/meme_detail.html'


class MemeCreationView(TemplateView):
    model = Meme
    template_name = 'memes/meme_creation.html'

    def get(self, request):
        self.form = MemeForm()
        return render(request, self.template_name, {'form': self.form})

    def post(self, request):
        self.form = MemeForm(request.POST, request.FILES)
        if self.form.is_valid():
            # Save model to database
            self.form.save()

            # Add success message
            messages.add_message(request, messages.SUCCESS, 'Meme created successfully.')
            return HttpResponseRedirect('/memes/create_meme/')
        return render(request, 'memes/meme_creation.html', {'form': self.form})

from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView, TemplateView

from meme_hunt.lib.time import TimeConverter
from scoreboard.models import Find
from scoreboard.views import ScoreboardView

from .models import Meme
from .forms import MemeForm

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


class MemeLocateView(TemplateView):
    model = Meme
    context_object_name = 'meme'
    template_name = 'memes/meme_locate.html'

    def get(self, request, secret_key):
        if request.user.is_authenticated:
            # First, check if the meme is the latest one
            latest_meme = Meme.latest()
            if latest_meme.secret_key != secret_key:
                messages.add_message(
                        request,
                        messages.ERROR,
                        'You can\'t locate past memes.')

            # Next, check that the Find occurs in the latest meme's time window
            now = TimeConverter.now()
            start_date = TimeConverter.min(latest_meme.start_date)
            end_date = TimeConverter.max(latest_meme.end_date)

            # Handle the strange case that a Find occurs before the start date
            if now < start_date:
                messages.add_message(request, messages.ERROR,
                        'You can\'t locate memes in the future.')
                return HttpResponseRedirect(reverse('scoreboard'))

            # Handle the case where a Find occurs after the end date
            if now > end_date:
                messages.add_message(
                        request,
                        messages.ERROR,
                        "The time has passed to find this meme")
                return HttpResponseRedirect(reverse('scoreboard'))

            # Finally, check whether the user has found the meme before
            meme = Meme.objects.filter(secret_key=secret_key).first()
            possible_find = Find.objects.filter(user=request.user)
            if possible_find.count() == 0:
                new_find = Find(
                        meme=meme,
                        user=request.user,
                        date_found=now,
                        score=0)
                new_find.determine_score()
                new_find.save()
                messages.add_message(request, messages.SUCCESS,
                        'Congratulations on finding the meme! You earned '
                        + str(new_find.score) + ' points!')
            else:
                messages.add_message(request, messages.INFO,
                        'You\'ve already found this meme!')
            return HttpResponseRedirect(reverse('scoreboard'))
        else:
            messages.add_message(request, messages.WARNING,
                    'You must log in to register finding the meme.')
            return HttpResponseRedirect(reverse('account_login') + '?next=' + '../../memes/locate/' + str(secret_key)) # TODO relative format later?


class MemeCreationView(TemplateView):
    model = Meme
    template_name = 'memes/meme_creation.html'

    def get(self, request):
        self.form = MemeForm()
        return render(request, self.template_name, {'form': self.form})

    def post(self, request):
        # Create new instance of form
        self.form = MemeForm(request.POST, request.FILES)
        if self.form.is_valid():
            # Save model to database
            new_meme = self.form.save()

            # Add success message
            messages.add_message(request, messages.SUCCESS, 'Meme created successfully.')
            return render(request, self.template_name, {'form': self.form, 'meme': new_meme})
        return render(request, 'memes/meme_creation.html', {'form': self.form})

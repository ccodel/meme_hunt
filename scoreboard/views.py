from django.contrib import messages
from django.shortcuts import render
from django.views.generic import ListView

from .models import Find
from memes.models import Meme

class ScoreboardView(ListView):
    model = Find
    context_object_name = 'find_list'
    template_name = 'scoreboard/scoreboard.html'

    # Retrives finds for the current meme, the past four memes,
    #   and all memes ever found.
    #
    # Loops through the finds and "pulls them forward" in time, summing scores
    def get(self, request):
        # Current meme's finds is easy - filter, sort by score
        latest_meme = Meme.latest()
        week_finds = Find.objects.filter(meme=latest_meme).order_by('-score')

        # Filter by latest four memes
        latest_four = Meme.latest_set(4)
        fourth_finds = Find.objects.filter(
                meme__in=latest_four).order_by('date_found')

        # Loop through past to future, keeping a dictionary by user email
        fourth_user_finds = {}
        for find in fourth_finds:
            # If not found this user before, add to dictionary
            if fourth_user_finds.get(find.user.email, None) is None:
                fourth_user_finds[find.user.email] = find
            else: # Modify score of existing find
                score = fourth_user_finds[find.user.email].score + find.score
                fourth_user_finds[find.user.email].score = score

        month_finds = list(fourth_user_finds.values())
        month_finds.sort(reverse=True, key=lambda f: f.score)

        # Loop through all finds, same thing
        all_finds = Find.objects.all().order_by('date_found')
        all_user_finds = {}
        for find in all_finds:
            if all_user_finds.get(find.user.email, None) is None:
                all_user_finds[find.user.email] = find
            else:
                score = all_user_finds[find.user.email].score + find.score
                all_user_finds[find.user.email].score = score

        all_finds = list(all_user_finds.values())
        all_finds.sort(reverse=True, key=lambda f: f.score)

        find_count = len(week_finds) + len(month_finds) + len(all_finds)

        return render(request, self.template_name, 
                {'week_finds': week_finds, 
                 'month_finds': month_finds,
                 'all_finds': all_finds,
                 'finds': find_count})

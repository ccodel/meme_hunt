from django.db import models
from datetime import datetime, time
from django.utils import timezone

class Find(models.Model):
    # Django provides default ID field
    meme = models.ForeignKey(
        'memes.Meme',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE
    )
    date_found = models.DateTimeField()
    score = models.IntegerField()

    def determine_score(self):
        # Determine base score based on time
        midnight = timezone.make_aware(
                timezone.datetime.combine(self.meme.start_date, time.min),
                timezone.get_current_timezone())
        difference = self.date_found - midnight
        hours_since = int(difference.total_seconds() // 3600)
        print('Hours since start date: ' + str(hours_since))
        score = max(0, 168 - hours_since)

        # Find all finds that occurred on this meme before date
        finds_before = Find.objects.filter(
                meme=self.meme,
                date_found__lt=self.date_found)

        # Hacked-in switch-case statement
        place_scores = {
            0: 500,
            1: 400,
            2: 350,
            3: 300,
            4: 250,
            5: 200,
            6: 175,
            7: 150,
            8: 125,
            9: 100,
            10: 75,
            11: 70,
            12: 65,
            13: 60,
            14: 55,
            15: 50,
            16: 45,
            17: 40,
            18: 35,
            19: 30
        }
        score = score + place_scores.get(finds_before.count(), 25)
        
        # Assign new score and save
        self.score = score


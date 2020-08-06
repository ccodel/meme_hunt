import uuid
import random
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site

def generate_random_key():
    return str(random.randint(1, 9999999))

class Meme(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False)
    subtitle = models.CharField(max_length=100)
    start_date = models.DateField(unique=True)
    end_date = models.DateField(unique=True)
    image = models.ImageField(upload_to="memes/") # TODO off MEDIA_URL?
    hint1 = models.CharField(max_length=100)
    hint2 = models.CharField(max_length=100)
    hint3 = models.CharField(max_length=100)
    hint4 = models.CharField(max_length=100)
    hint5 = models.CharField(max_length=100)
    hint6 = models.CharField(max_length=100)
    hint7 = models.CharField(max_length=100)
    secret_key = models.UUIDField(
            unique=True,
            default=uuid.uuid4)

    def __str__(self):
        return self.subtitle

    def get_absolute_url(self):
        return reverse('meme_detail', args=[str(self.id)])

    # Prepends with SITE_ID
    def get_absolute_location_url(self):
        return get_current_site(None).domain + reverse(
                'meme_locate', args=[str(self.secret_key)])

    # Finds the most recent meme
    @staticmethod
    def latest():
        return Meme.objects.latest('start_date')

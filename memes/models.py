import uuid
import random

from django.db import models
from django.urls import reverse
from django.conf import settings
from django.core.exceptions import ValidationError
from django.contrib.sites.shortcuts import get_current_site

# Validator for Meme dates. Memes cannot overlap in their date ranges.
# TODO does not catch Memes 'date-internal' to others.
def validate_date(date):
    memes_for_start_range = Meme.objects.filter(
            start_date__lte=date,
            end_date__gte=date)
    if memes_for_start_range.count() > 0:
        raise ValidationError(str(date) + ' overlaps with another meme\'s date range. Try another date.')


class Meme(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False)
    subtitle = models.CharField(max_length=100)
    start_date = models.DateField(unique=True, validators=[validate_date])
    end_date = models.DateField(unique=True, validators=[validate_date])
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

    def hints(self):
        return { self.hint1,
                self.hint2,
                self.hint3,
                self.hint4,
                self.hint5,
                self.hint6,
                self.hint7 }

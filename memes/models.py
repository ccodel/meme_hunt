import uuid
from django.db import models
from django.urls import reverse
from django.conf import settings

class Meme(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False)
    subtitle = models.CharField(max_length=100, unique_for_date="start_date")
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to="memes/") # TODO off MEDIA_URL?
    hint1 = models.CharField(max_length=100)
    hint2 = models.CharField(max_length=100)
    hint3 = models.CharField(max_length=100)
    hint4 = models.CharField(max_length=100)
    hint5 = models.CharField(max_length=100)
    hint6 = models.CharField(max_length=100)
    hint7 = models.CharField(max_length=100)

    def __str__(self):
        return self.subtitle

    def get_absolute_url(self):
        return reverse('meme_detail', args=[str(self.id)])

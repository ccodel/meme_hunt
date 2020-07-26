import uuid
from django.db import models
from django.urls import reverse

class Meme(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False)
    subtitle = models.CharField(max_length=200, unique_for_date="start_date")
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to="") # TODO Figure out URL for this
    hint1 = models.CharField(max_length=200)
    hint2 = models.CharField(max_length=200)
    hint3 = models.CharField(max_length=200)
    hint4 = models.CharField(max_length=200)
    hint5 = models.CharField(max_length=200)
    hint6 = models.CharField(max_length=200)
    hint7 = models.CharField(max_length=200)

    def __str__(self):
        return self.subtitle

    def get_absolute_url(self):
        return reverse('meme', args[str(self.id)])

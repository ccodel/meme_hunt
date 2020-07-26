from django.contrib.auth.models import AbstractUser
from django.db import models

# Extends Django auth's AbstractUser. Custom user for meme_hunt.
class CustomUser(AbstractUser):
    pass

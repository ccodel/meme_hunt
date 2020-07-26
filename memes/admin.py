from django.contrib import admin
from .models import Meme

class MemeAdmin(admin.ModelAdmin):
    list_display = ("subtitle", "start_date",)

admin.site.register(Meme, MemeAdmin)

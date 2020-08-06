from django.contrib import admin
from .models import Find

class FindAdmin(admin.ModelAdmin):
    list_display = ('user', 'meme',)

admin.site.register(Find, FindAdmin)

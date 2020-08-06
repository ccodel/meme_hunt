from django import forms

from .models import Meme

class DateInput(forms.DateInput):
    input_type = 'date'

"""
Create a new meme
"""
class MemeForm(forms.ModelForm):
    class Meta:
        model = Meme
        fields = ['subtitle', 'start_date', 'end_date', 'image', 'hint1', 'hint2', 'hint3', 'hint4', 'hint5', 'hint6', 'hint7', 'secret_key']
        widgets = {'secret_key': forms.HiddenInput()}

    # Override default input types for date fields
    start_date = forms.DateField(label='Start date', widget=DateInput())
    end_date = forms.DateField(label='End date', widget=DateInput())

    # def __init__(self, request_post, request_files):
    #    self.secret_key.value

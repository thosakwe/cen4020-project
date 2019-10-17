from django import forms
from django.contrib.auth.models import User

class NewGameForm(forms.Form):
    description = forms.CharField()
    image = forms.ImageField()
    title = forms.CharField()

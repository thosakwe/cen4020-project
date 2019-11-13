from django import forms
from .models import playthroughs


class VideoForm(forms.ModelForm):
    class Meta:
        model = playthroughs
        fields= ["name", "videofile"]
from .models import Comment, ReviewVote
from django import forms

"""
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
"""
class CommentForm(forms.Form):
    content = forms.CharField()

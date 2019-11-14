from .models import Comment, Like, ReviewVote
from django import forms

"""
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
"""
class CommentForm(forms.Form):
    content = forms.CharField()

class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        exclude = '__all__'
        widgets = {'user': forms.HiddenInput(),'review': forms.HiddenInput(),}

class ReviewVoteForm(forms.ModelForm):
    class Meta:
        model = Like
        exclude = '__all__'
        widgets = {'user': forms.HiddenInput(),'review': forms.HiddenInput(),'vote': forms.HiddenInput(),}

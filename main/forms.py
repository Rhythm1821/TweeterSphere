from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    body = forms.CharField(label="",required=True,
                           widget=forms.widgets.Textarea(
                               attrs={
                                   "placeholder":"Enter your tweet",
                                   "class":"form-control",
                               }
                           ))
    class Meta:
        model=Tweet
        exclude=('User',)
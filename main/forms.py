from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tweet,Profile


class ProfileImageForm(forms.ModelForm):
    profile_image = forms.ImageField(label="Profile Picture")

    class Meta:
        model = Profile
        fields = ('profile_image', )

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

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='',max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserUpdateForm(UserCreationForm):
    email = forms.EmailField(label='',max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']        
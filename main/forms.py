from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tweet,Profile


class ProfileImageForm(forms.ModelForm):
    profile_image = forms.ImageField(label="Profile Picture",required=False)
    profile_bio = forms.CharField(label='Profile Bio',required=False,widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Profile Bio'}))
    homepage_link = forms.CharField(label='',required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Website Link'}))
    instagram_link = forms.CharField(label='',required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Instagram Link'}))
    facebook_link = forms.CharField(label='',required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Facebook Link'}))
    linkedin_link = forms.CharField(label='',required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Linkedin Link'}))


    class Meta:
        model = Profile
        fields = ('profile_image', 'profile_bio','homepage_link','instagram_link','facebook_link','linkedin_link')

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
        exclude=('user','likes')

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='',max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    password1 = forms.CharField(label='New Password', max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Password'}), required=False)
    password2 = forms.CharField(label='Confirm New Password', max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm New Password'}), required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

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

    # def clean_password2(self):
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 != password2:
    #         raise forms.ValidationError("Passwords do not match")
    #     return password2

    # def clean_password1(self):
    #     password1 = self.cleaned_data.get("password1")
    #     if len(password1) < 8:
    #         raise forms.ValidationError("Password must be at least 8 characters long")
    #     return password1     
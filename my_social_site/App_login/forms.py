from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse,reverse_lazy
from .models import UserProfile


class CreateNewUser(UserCreationForm):
    email=forms.EmailField(required=True,label="Email",widget=forms.TextInput(attrs={'placeholder':'Email'}))
    username=forms.CharField(required=True,label="Username",widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password1=forms.CharField(required=True,label="Password",widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2=forms.CharField(required=True,label="Confirm Password",widget=forms.PasswordInput(attrs={'placeholder':'Confirm password'}))
    class Meta:
        model=User
        fields=('email','username','password1','password2')


class EditProfile(forms.ModelForm):
    dob=forms.DateField(widget=forms.TextInput(attrs={'type':'date',}))
    class Meta:
        model=UserProfile()
        exclude=('user',)

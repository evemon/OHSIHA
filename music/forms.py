from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    #metadata about class
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserLogin(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    #metadata about class
    class Meta:
        model = User
        fields = ['username','password']

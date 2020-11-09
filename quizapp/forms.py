from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class participantForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model=User
        fields=('username','email','password')
        full_name= forms.CharField(max_length=100)

class quizMasterForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model=User
        fields=('username','email','password')
        full_name= forms.CharField(max_length=100)

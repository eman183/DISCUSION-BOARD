from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email=forms.CharField(max_length=100,required=True
                          ,widget=forms.EmailInput)
    
    class Mets:
        model=User
        fields={"username","email","password1",""}
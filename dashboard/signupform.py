# forms.py
from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=100)
    firstname = forms.CharField(max_length=100,label="Name")
    lastname = forms.CharField(max_length=100 , label="")
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirmationpassword = forms.CharField(widget=forms.PasswordInput , label="Confirmation Password")

from django import forms

class SignInForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Type your Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Type your Password'}), label="")

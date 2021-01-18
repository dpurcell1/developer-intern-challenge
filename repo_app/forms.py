from PIL import Image
from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

class UploadForm(forms.Form):    
    image = forms.ImageField()
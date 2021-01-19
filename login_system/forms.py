from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    #username = forms.CharField(label="Username",max_length=100)
    #password = forms.CharField(label="password",max_length=32, widget=forms.PasswordInput)
    #confirm_password = forms.CharField(label="confirm password",max_length=32, widget=forms.PasswordInput)
    """def clean(self):
        cleaned_data = super().clean()
        p = self.cleaned_data.get("password")
        cp = self.cleaned_data.get("confirm_password")

        if p!= cp:
            raise forms.ValidationError("Passwords don't match")
            """

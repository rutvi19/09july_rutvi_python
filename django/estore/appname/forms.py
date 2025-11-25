from django import forms
from .models import UserSignup

class SignupForm(forms.ModelForm):
    class Meta:
        model = UserSignup
        fields = '__all__'



class LoginForm(forms.Form):
    Emailaddress= forms.CharField(max_length=100)
    password = forms.CharField(max_length=50)

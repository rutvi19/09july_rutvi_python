from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model=Userdata
        fields='__all__'
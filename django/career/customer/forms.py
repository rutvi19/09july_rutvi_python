from .models import *
from django import forms

class register_form(forms.ModelForm):
    class Meta:
        model=user_register
        fields = '__all__'
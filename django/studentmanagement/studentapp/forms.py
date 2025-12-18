from django import forms
from .models import *


class data(forms.ModelForm):
    class Meta:
        model=stdata
        fields='__all__'
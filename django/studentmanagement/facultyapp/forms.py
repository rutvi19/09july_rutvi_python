from django import forms
from .models import *


class faform(forms.ModelForm):
    class Meta:
        model=fa_data
        fields='__all__'
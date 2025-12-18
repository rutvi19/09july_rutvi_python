from .models import *
from django import forms

class artist_form(forms.ModelForm):
    class Meta:
        model=register_artist
        fields = '__all__'
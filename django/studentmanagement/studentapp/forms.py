from django import forms
from .models import *


class stdform(forms.ModelForm):
    class Meta:
        model=stdata
        fields='__all__'

class courseform(forms.ModelForm):
    class Meta:
        model = std_course
        fields = ['course']

class contactform(forms.ModelForm):
    class Meta:
        model = contact_std_cls
        fields = ['message','image']

class notesform(forms.ModelForm):
    class Meta:
        model = notes_cls
        fields = ['title', 'description']

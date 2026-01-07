from django import forms
from .models import *

class notesform(forms.ModelForm):
    class Meta:
        model = note_cls
        fields = '__all__'
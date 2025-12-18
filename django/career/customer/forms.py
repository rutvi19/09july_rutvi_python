from .models import *
from django import forms

class register_form(forms.ModelForm):
    class Meta:
        model=user_register
        fields = '__all__'

class manage_booking_form(forms.ModelForm):
    class Meta:
        model=manage_booking_cls
        fields = ['artist_name']        

class feedback_form(forms.ModelForm):
    class Meta:
        model = feedback_cls
        fields = ['feedback']        
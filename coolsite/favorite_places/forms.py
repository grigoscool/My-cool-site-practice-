from django import forms
from .models import *
class AddPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields ='__all__'




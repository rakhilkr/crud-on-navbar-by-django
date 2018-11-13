from django import forms
from home.models import *

class contactform(forms.ModelForm):

    class Meta:
        model= contact
        fields= ["name", "email", "phone", "message"]
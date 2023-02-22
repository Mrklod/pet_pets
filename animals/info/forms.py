from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'age','text','nickname','category']
from django import forms
from .models import *

class ScanTextForm(forms.ModelForm):
    class Meta:
        model = ScanedTextImage
        fields = ('image',)

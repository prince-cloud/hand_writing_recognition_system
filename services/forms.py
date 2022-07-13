from django import forms
from .models import *


class ScanTextForm(forms.ModelForm):
    class Meta:
        model = ScanedTextImage
        fields = ("image",)


class TranslateTextForm(forms.ModelForm):
    class Meta:
        model = TranslateText
        fields = (
            "text",
            "translate_to",
        )
        widgets = {
            "text": forms.Textarea(attrs={"rows": 4, "cols": 15}),
        }


class TextToSpeechForm(forms.ModelForm):
    class Meta:
        model = TextToSpeech
        fields = ("text",)
        widgets = {
            "text": forms.Textarea(attrs={"rows": 4, "cols": 15}),
        }

from django import forms
from django.core import validators

class TextForm(forms.Form):

    sentence = forms.CharField(widget=forms.Textarea)
    WordCount = forms.BooleanField(required=False)
    LineCount = forms.BooleanField(required=False)
    LetterCount = forms.BooleanField(required=False)
    Frequences = forms.BooleanField(required=False)

    def __str__(self) -> str:
        return self.sentence
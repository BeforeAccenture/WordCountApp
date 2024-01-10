from django import forms
from django.core import validators

class TextForm(forms.Form):

    sentence = forms.CharField(widget=forms.Textarea(attrs={'oninput':'countWords()',
                                                            'style':'min-height:350px;margin-bottom:10px',
                                                            'class':'form-control','placeholder':'Please Enter text here...'}))
    # WordCount = forms.BooleanField(required=False)
    # LineCount = forms.BooleanField(required=False)
    # LetterCount = forms.BooleanField(required=False)
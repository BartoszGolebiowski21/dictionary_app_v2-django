from django import forms

from .models import Word

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ["english_translation", "english_pronunciation", "polish_translation",]
        labels = {
            "english_translation": "English translation",
            "english_pronunciation": "English pronunciation (optional)",
            "polish_translation": "Polish translation",
        }

class TestForm(forms.Form):
    entered_word = forms.CharField(max_length=80)
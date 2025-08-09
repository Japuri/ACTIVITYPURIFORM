from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content', 'image']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        prohibited_words = ['shit', 'fuck', 'bobo']

        for word in prohibited_words:
            if word.lower() in content.lower():
                raise forms.ValidationError(f"The word '{word}' is not allowed.")
        return content

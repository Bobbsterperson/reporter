from django import forms
from .models import Submission

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'Type something...'}),
        }

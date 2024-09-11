from django import forms
from .models import Submission, Journal

class SubmissionForm(forms.ModelForm):
    journal_name = forms.CharField(max_length=100, required=True, label='Journal Name', help_text='Enter the journal name.')

    class Meta:
        model = Submission
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'Type something...'}),
        }
    
    def save(self, commit=True):
        journal_name = self.cleaned_data.get('journal_name')
        journal, created = Journal.objects.get_or_create(name=journal_name)
        submission = super().save(commit=False)
        submission.journal = journal
        if commit:
            submission.save()
        return submission

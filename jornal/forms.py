from django import forms
from .models import Submission, Journal, Tag

class SubmissionForm(forms.ModelForm):
    journal_name = forms.CharField(max_length=100, required=True, label='Journal Name', help_text='Enter the journal name.')
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Tags'
    )
    new_tags = forms.CharField(
        max_length=255,
        required=False,
        help_text='Enter new tags separated by commas.'
    )

    class Meta:
        model = Submission
        fields = ['text', 'journal_name', 'tags', 'new_tags']
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'Type something...'}),
        }

    def save(self, commit=True):
        journal_name = self.cleaned_data.get('journal_name')
        journal, created = Journal.objects.get_or_create(name=journal_name)

        # Save the submission
        submission = super().save(commit=False)
        submission.journal = journal
        if commit:
            submission.save()
            self.save_m2m()  # Save the many-to-many data for the form.

        # Process new tags
        new_tags = self.cleaned_data.get('new_tags')
        if new_tags:
            tag_names = [tag.strip() for tag in new_tags.split(',')]
            for tag_name in tag_names:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                submission.tags.add(tag)

        return submission

from django import forms
from django.core.exceptions import ValidationError
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """
    Form for handling recruiter, client, and collaboration contact inquiries.
    Includes input sanitization, required field checks, and anti-spam honeypot.
    """
    # Honeypot field hidden from humans via CSS and tab index - bots fill this in
    website_url = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'd-none',
            'tabindex': '-1',
            'autocomplete': 'off',
            'aria-hidden': 'true',
        })
    )

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Full Name (e.g. John Doe)',
                'autocomplete': 'name',
                'required': True,
                'aria-label': 'Full Name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email Address (e.g. name@company.com)',
                'autocomplete': 'email',
                'required': True,
                'aria-label': 'Email Address',
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subject (e.g. IT Internship Opportunity / Collaboration)',
                'required': True,
                'aria-label': 'Subject',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Type your message, role details, or question here...',
                'required': True,
                'aria-label': 'Message Content',
            }),
        }
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'subject': 'Subject',
            'message': 'Message',
        }

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if len(name) < 2:
            raise ValidationError("Please provide a valid name (at least 2 characters).")
        return name

    def clean_subject(self):
        subject = self.cleaned_data.get('subject', '').strip()
        if len(subject) < 3:
            raise ValidationError("Please provide a subject line (at least 3 characters).")
        return subject

    def clean_message(self):
        message = self.cleaned_data.get('message', '').strip()
        if len(message) < 10:
            raise ValidationError("Please write a meaningful message (at least 10 characters).")
        return message

    def clean(self):
        cleaned_data = super().clean()
        honeypot = cleaned_data.get('website_url')
        if honeypot:
            raise ValidationError("Spam submission detected and rejected.")
        return cleaned_data

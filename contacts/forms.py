from django import forms

class ContactForm(forms.Form):
    yourname=forms.CharField('Your Name')
    email=forms.EmailField)(required=True, 'Your Email address')
    subject=forms.CharField(required=False)
    message=forms.Textarea()
from django import forms

class ContactForm(forms.Form):
    yourname=forms.CharField(label ='Your Name')
    email=forms.EmailField( label ='Your email address',required=False)
    subject=forms.CharField()
    message=forms.CharField( label='Message',widget=forms.Textarea)
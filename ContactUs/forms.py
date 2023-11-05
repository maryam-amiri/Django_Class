
from django import forms
from form import form

from ContactUs.models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['title', 'email', 'name' , 'message']

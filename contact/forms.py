__author__ = 'Hernan Y.Ke'
from django import forms

class contactForm(forms.Form):
    name = forms.CharField(required=False, max_length=100, help_text='100 char')
    email = forms.EmailField(required=True)
    comment = forms.CharField(required=True, widget=forms.Textarea)
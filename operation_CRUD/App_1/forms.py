from django import forms
from App_1.models import user
from django.core import validators

class Stud(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=user
        fields=['name','email','password']

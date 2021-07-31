from django import forms

from db_demo.models import book_Demo


class userRegistration(forms.Form):
    s_Name=forms.CharField(max_length=20)
    s_Marks=forms.IntegerField()

class book_Form(forms.ModelForm):
    class Meta:
        model= book_Demo
        fields="__all__"
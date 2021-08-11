from django import forms

class person_Info(forms.Form):
    p_name=forms.CharField(max_length=20)
    p_sal=forms.FloatField()
    p_gender=forms.CharField(max_length=6)

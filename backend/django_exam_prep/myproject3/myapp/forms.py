from django import forms

class contactform(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    age = forms.IntegerField()
from django import forms

class contactform(forms.Form):

    name = forms.CharField(max_length=100)
#   last_name = forms.CharField(max_length=100)

    email = forms.EmailField()

    def clean_name(self):

        name = self.cleaned_data['name']

        if len(name) < 3:
            raise forms.ValidationError("Name too short")

        return name
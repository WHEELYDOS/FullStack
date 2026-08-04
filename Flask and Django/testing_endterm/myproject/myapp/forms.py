from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()

#custom validation 
    def clean_name(self):
        name = self.cleaned_data['name']

        if len(name) < 3:
            raise forms.ValidationError("Name too short")

        return name
from django import forms

class UrlForm(forms.Form):
    len_choices = [(i,i) for i in range(3,21)]
    url = forms.URLField(label="Insert URL:")
    len = forms.ChoiceField(choices=len_choices, initial=6,
                            label="How many characters use to generate the link?")

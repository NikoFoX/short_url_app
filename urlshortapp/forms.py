from django import forms

class UrlForm(forms.Form):
    len_choices = list()
    for i in range(3, 21):
        len_choices.append((i, i))
    url = forms.URLField(label="Insert URL:")
    len = forms.ChoiceField(choices=(len_choices), initial=6,
                            label="How many characters use to generate the link?")

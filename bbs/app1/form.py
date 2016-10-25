from django import forms

class NameForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
    myfile = forms.FileField(required=False)


class UserForm(forms.Form):
    name = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)

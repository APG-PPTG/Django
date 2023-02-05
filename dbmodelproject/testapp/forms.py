from django import forms

class JobApplicationForm(forms.Form):
    name = forms.CharField(max_length=20)
    email= forms.EmailField()
    phNo = forms.IntegerField()

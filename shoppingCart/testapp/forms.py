from django import forms

class AddItemsForm(forms.Form):
    itemname = forms.CharField(max_length=20)
    quantity = forms.IntegerField()

from django import forms

class Form(forms.Form):
     text = forms.CharField(widget=forms.Textarea)
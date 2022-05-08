from django import forms

class Form(forms.Form):
     choice = [('normal','Normal'),('ratio','Ratio'),('count','Word Count')]
     text = forms.CharField(widget=forms.Textarea)
     text.widget.attrs.update({'class':'form-control  px-3'})
     select = forms.CharField(label='Type', widget=forms.Select(choices=choice))
     select.widget.attrs.update({'id':'select',"onChange":'e()','class':'form-control  px-3'})

     count = forms.DecimalField(max_digits=4, decimal_places=0,required=False)
     count.widget.attrs.update({'class':'form-control  px-3'})
     ratio = forms.DecimalField(max_digits=2, decimal_places=0,required=False)
     ratio.widget.attrs.update({'class':'form-control  px-3'})

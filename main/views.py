from django.http import HttpResponse
from django.shortcuts import render
from .forms import Form 
from . import summerize
def index(request):
    content = {}
    form = Form
    content = {'form': form}
    if request.method =='POST':
        f = Form(request.POST)
        if f.is_valid():
            text = f.cleaned_data['text']
            content={'form': form,
            'summerized':summerize.summerize(text)}
            return render(request,"main/index.html",content)
    return render(request,"main/index.html",content)

  

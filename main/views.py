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
            select = f.cleaned_data['select']
            count = f.cleaned_data['count']
            ratio = f.cleaned_data['ratio']
            
            if select =='normal':
                summerized = summerize.summerize(text)
            if select == 'ratio':
                ratio=int(ratio)/100
                summerized = summerize.summerizeByRatio(text,ratio)
            if select == 'count':
                summerized = summerize.summerizeByWordCount(text,count)
            original_count = summerize.word_count(text)
            summerized_count  = summerize.word_count(summerized)
            percent = round((summerized_count*100)/original_count,2)
            p = round(summerize.precision(text,summerized),2)
            content={'form': form,
            'summerized':summerized,
            'text':text,
            'ori_count':original_count,
            'sum_count':summerized_count,
            'percent':percent,
            'p':p}
            return render(request,"main/index.html",content)
    return render(request,"main/index.html",content)

  

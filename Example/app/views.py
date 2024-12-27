from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from app.forms import *
from django.http import HttpResponse

def UserForm(request):
    EUFO=UserModelForm()
    d={'EUFO':EUFO}
    if request.method =='POST':
        DUFO=UserModelForm(request.POST)
        if DUFO.is_valid():
            DUFO.save()
            return HttpResponse('Successfull...')
        else:
            return HttpResponse('Provide Valid Data')
    return render(request,'UserForm.html',d)
        
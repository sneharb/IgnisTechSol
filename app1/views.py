from django.shortcuts import render 
from .forms import EventForm
from .models import *
import pyautogui as pu

# Create your views here.

def index(request):
    Events = Event.objects.all()
    context = {'Events': Events}
    return render(request, 'app1/main.html', context)

def register(request):
    if request.method == 'POST':
        form=EventForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        pu.confirm("Your event is registered.Thank you!")
        return render(request, 'app1/main.html',{'form':form})
    else:
        form=EventForm()
        return render(request, 'app1/register.html',{'form':form})


from django.shortcuts import render
from . models import Place
from .models import Team


# Create your views here.

def home(request):
    obj = Place.objects.all()
    obj1 = Team.objects.all()
    return render(request,"home.html" ,{'result':obj, 'team':obj1})

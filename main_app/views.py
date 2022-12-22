from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Lion



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def lions_index(request):
    lions = Lion.objects.all()
    return render(request, 'lions/index.html', {'lions': lions})

def lions_detail(request, lion_id):
   lion = Lion.objects.get(id=lion_id)
   return render(request,'lions/detail.html', {'lion':lion})
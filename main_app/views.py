from django.shortcuts import render

#import the clbv
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
from django.http import HttpResponse
from .models import Lion



class LionUpdate(UpdateView):
  model = Lion
  # disallow the update of the name
  fields = ['breed', 'description', 'age']
  # the is redirect happens on the model def get_absolute_url


class LionDelete(DeleteView):
  model = Lion
  # want to define the success_url, since when we delete something we can't redirect to the detail page
  success_url = '/lions/'

class LionCreate(CreateView):
    model = Lion

    fields = '__all__' 



def home(request):
	return render(request, 'home.html')


def about(request):
	return render(request, 'about.html')


def lions_index(request):
  lions = Lion.objects.all()
  return render(request, 'lions/index.html', {'lions': lions})


def lions_detail(request, lion_id):

  lion = Lion.objects.get(id=lion_id)
  
  return render(request, 'lions/detail.html', {'lion': lion})
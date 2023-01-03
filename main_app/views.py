from django.shortcuts import render, redirect

#import the clbv
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# Create your views here.
from django.http import HttpResponse
from .models import Lion, Toy
from .forms import FeedingForm

def add_feeding(request, lion_id):
    form = FeedingForm(request.POST)
    if form.is_valid(): 
        new_feeding = form.save(commit=False)
        new_feeding.lion_id = lion_id
        new_feeding.save()
    return redirect('detail', lion_id=lion_id)



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

    fields = ['name', 'breed', 'description', 'age']



def home(request):
	return render(request, 'home.html')


def about(request):
	return render(request, 'about.html')


def lions_index(request):
  lions = Lion.objects.all()
  return render(request, 'lions/index.html', {'lions': lions})


def lions_detail(request, lion_id):

  lion = Lion.objects.get(id=lion_id)
  toys_lion_doesnt_have = Toy.objects.exclude(id__in = lion.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  
  return render(request, 'lions/detail.html', {'lion': lion,'feeding_form': feeding_form, 'toys': toys_lion_doesnt_have})

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'

def assoc_toy(request, lion_id, toy_id):
  # Note that you can pass a toy's id instead of the whole object
  Lion.objects.get(id=lion_id).toys.add(toy_id)
  return redirect('detail', lion_id=lion_id)
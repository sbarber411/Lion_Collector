from django.shortcuts import render

# Add the following import
from django.http import HttpResponse


# Add the lion class & list and view function below the imports
class Lion:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

lions = [
  Lion('King', 'african lion', 'male', 3),
  Lion('Queen', 'african lioness', 'female', 3),
  Lion('Leo', 'white lion', 'white lion', 1)
]


# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def lions_index(request):
    return render(request, 'lions/index.html', { 'lions': lions })


from django.shortcuts import render

# Add the Cat class & list and view function below the imports
class Dogs:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dogs = [
  Dogs('Lola', 'English Bulldog', 'always hungry', 3),
  Dogs('Reno', 'Pitbull', 'full of energy', 2),
  Dogs('Bud', 'Golden Retriever', 'Movie Star', 4)
]


# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello</h1>')

def about(request):
  return render(request, 'about.html')

def dogs_index(request):
  return render(request, 'dogs/index.html', {'dogs': dogs})
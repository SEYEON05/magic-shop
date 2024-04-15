from django.shortcuts import render
from magic.models import Category, Power

def index(request):
  category = Category.objects.all
  power = Power.objects.all
  context = {
    'category' : category,
    'power': power

  }
  return render(request, 'index.html', context=context)
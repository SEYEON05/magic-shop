from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import generic
from .models import *
from django.views.decorators.http import require_http_methods
from django.core.files.storage import FileSystemStorage

def index(request):
  if request.method=='POST':  # 두 가지 메소드 방식에 대해 화면 출력을 정의해주어야 함.
    category = Category.objects.get(name=request.POST['category'])  
    
    uploaded_file = request.FILES['file']
    fs = FileSystemStorage()
    name = fs.save(uploaded_file.name, uploaded_file)
    url = fs.url(name)
    Power.objects.create(category=category, name=request.POST['powername'], description=request.POST['context'],image_url=url).save()
    return redirect('index') # 폼 제출 후 표현할 화면
  
  # elif request.method=='GET':  ## 생략됨
  #   pass
  
  return render(request=request, template_name='magic/add_product.html')

def detail(request, pk):
  category = Category.objects.get(pk=pk)
  context = {
    'category': category,
  }
  return render(request=request, template_name='magic/detail.html', context=context)

def power_detail(request, pk):
  power = Power.objects.get(pk=pk)
  context = {
    'power': power,
  }
  return render(request, 'magic/power_detail.html', context)

def power_delete(request, pk):
  power = Power.objects.get(pk=pk)
  power.delete()
  return redirect('index')

# @require_http_methods(["GET", "POST"])
# def upload_file(request):
#     if request.method == 'POST':
#         uploaded_file = request.FILES['file']
#         fs = FileSystemStorage()
#         name = fs.save(uploaded_file.name, uploaded_file)
#         url = fs.url(name)
#         return HttpResponse(f"File uploaded at {url}")
#     return render(request, 'upload.html')

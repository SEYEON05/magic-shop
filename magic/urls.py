from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'magic'
urlpatterns = [
    path('', index, name='add_product'),
    path('cate/<int:pk>/', detail, name='detail'),
    path('power/<int:pk>/', power_detail, name='power_detail'),
    path('delete/<int:pk>/', power_delete, name='delete')
]

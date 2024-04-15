from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=20)

class Power(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  name = models.CharField(max_length=50)
  description = models.TextField(default='준비 중..')
  image_url = models.URLField()
from django.db import models

# Create your models here.
class Collection(models.Model):
  img = models.ImageField(upload_to='products')
  title = models.CharField(max_length=100)
  price = models.IntegerField()
  desc = models.TextField()
  reviews = models.IntegerField()

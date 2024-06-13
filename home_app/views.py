from django.shortcuts import render
from .models import Collection


def homepage(request):
  collection = Collection.objects.all()

  return render(request, 'index.html', {'collection': collection})

def view_product(request, id):
  product_id = Collection.objects.get(id=id)

  return render(request, 'checkout.html', {'product_id': product_id})

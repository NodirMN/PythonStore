from django.shortcuts import render

from products.models  import ProductCategory, Product


def index(request):
    context = {'title' : 'BestStore'}
    return render(request, 'products/index.html', context) 

def products(request):
    context = {
        'title' : 'Catalogs',
        'categories' : ProductCategory.objects.all(),
        'products' : Product.objects.all(),
        }
    return render(request, 'products/products.html', context) 


from django.shortcuts import render




def index(request):
    context = {'title' : 'BestStore'}
    return render(request, 'products/index.html', context) 

def products(request):
    context = {'title' : 'Catalogs'}
    return render(request, 'products/products.html', context) 


def test_context(request):
    context = {
        'title' : "Store",
        'header' : "Welcome our Store",
        'username' : "Nodir",
        'products' : [
            {
                'name' : 'Snikers',
                'price' : 20000
            },
            {
                'name' : 'Baunti',
                'price' : 10000
            }
        ]
    }
    return render(request, 'products/test_context.html', context) 
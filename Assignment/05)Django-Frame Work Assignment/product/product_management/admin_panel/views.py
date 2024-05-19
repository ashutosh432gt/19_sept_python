from django.shortcuts import render
from .models import Product

def home(request):
    query = request.GET.get('query', '')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    
    return render(request, 'admin_panel/home.html', {'products': products})

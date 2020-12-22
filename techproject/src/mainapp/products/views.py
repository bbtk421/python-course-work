from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

def admin_console(request):
    products = Product.objects.all()
    return render(request, 'products/products_page.html', {'products': products})

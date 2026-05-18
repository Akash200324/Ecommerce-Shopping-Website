from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'shop/home.html')

def street_flex(request):
    return render(request, 'shop/category/street-flex.html')
def simple_swag(request):
    return render(request, 'shop/category/simple-swag.html')

def fit_gear(request):
    return render(request, 'shop/category/fit-gear.html')

def add_to_cart(request):
    return render(request, 'shop/category/add-to-cart.html')
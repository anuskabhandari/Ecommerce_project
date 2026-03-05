from django.shortcuts import render, redirect
from .models import Product

def product_list(request):
    category = request.GET.get('category')
    if category:
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request,'product_detail.html',{'product':product})

def add_to_cart(request, id):
    cart = request.session.get('cart',[])
    cart.append(id)
    request.session['cart'] = cart
    return redirect('home')

def cart(request):
    cart = request.session.get('cart',[])
    products = Product.objects.filter(id__in=cart)
    return render(request,'cart.html',{'products':products})
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('home')
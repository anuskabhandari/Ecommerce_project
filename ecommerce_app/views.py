from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Product
from django.http import JsonResponse

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return render(request, 'register.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        return redirect('login')

    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def product_list(request):
    products = Product.objects.all()

    category = request.GET.get('category')
    if category:
        products = products.filter(category=category)

    return render(request,'product_list.html',{'products':products})

def product_detail(request,id):
    product = Product.objects.get(id=id)
    return render(request,'product_detail.html',{'product':product})

def add_to_cart(request, id):
    cart = request.session.get('cart', [])
    cart.append(id)
    request.session['cart'] = cart

    # Return JSON instead of redirect
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'message': 'Product added to cart', 'cart_count': len(cart)})
    else:
        return redirect('home')

def cart(request):
    cart = request.session.get('cart', [])
    products = Product.objects.filter(id__in=cart)

    # Calculate total
    total = sum(product.price for product in products)

    return render(request, 'cart.html', {'products': products, 'total': total})

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to homepage after logout
def remove_from_cart(request, id):
    cart = request.session.get('cart', [])
    if id in cart:
        cart.remove(id)
    request.session['cart'] = cart
    return redirect('cart')

def checkout(request):
    # Get the cart items from session or database
    cart_items = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart_items.values())

    # Here you can handle payment or order saving
    return render(request, 'checkout.html', {'cart_items': cart_items, 'total': total})
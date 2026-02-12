from django.shortcuts import render, redirect
from .models import Product, Person
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages import error, success

# Create your views here.

def homepage (request):
    product = Product.objects.all()
    q = request.GET.get ('q') if request.GET.get('q') != None else ''

    if q:
        product = Product.objects.filter (short_name_product__icontains=q)
    else:
        product = Product.objects.all()
    
    context = {
        "product":product
    }

    if request.user.is_superuser:
        logout (request)
        return redirect ("homepage_url")

    return render (request, "index.html", context)

def detailpage (request, pk):
    try:
        product = Product.objects.get (id=pk)
    except Product.DoesNotExist:
        return HttpResponse ("Product not found")
    
    context = {
        "product":product
    }

    return render (request, "detail.html", context)

def loginpage (request):
    if request.method == "POST":
        username = request.POST.get ("username")
        password = request.POST.get ("password")

        user = authenticate (username=username, password=password)
        if user is not None:
            login (request, user)
            return redirect ("homepage_url")
        else:
            error (request, "Username or Password is incorrect")
            return redirect ("login_url")
        
    return render (request, "login.html")

def logoutpage (request):
    logout (request)
    return redirect ("homepage_url")

def sign_up (request):
    if request.method == "POST":
        username = request.POST.get ("username")
        email = request.POST.get ("email")
        password = request.POST.get ("password")
        confirmpassword = request.POST.get ("confirmpassword")
        if password != confirmpassword:
            error (request, "Your Password Does Not Match!")
            return redirect ("sign_up_url")
        try:
            Person.objects.get(username=username)
            error(request, 'username already taken')
            return redirect('sign_up_url')
        except Person.DoesNotExist:
            user = Person.objects.create(
                username=username,
                email = email,
            )
            user.set_password(password)
            user.save()
            success(request, 'your account created successfully')
            return redirect('login_url')
    return render (request, "signup.html")
from django.shortcuts import render

# Create your views here.


def home(req):
    return render(req, 'home.html')


def index(req):
    return render(req, 'Index.html')


def cart(req):
    return render(req, 'cart1.html')


def product(req):
    return render(req, 'ProductPage.html')


def signup(req):
    return render(req, 'Login_RegPage.html')

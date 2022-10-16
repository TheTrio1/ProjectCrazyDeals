from django.shortcuts import render, redirect
from .models import Customer, User
from django.contrib.auth import login, logout
# Create your views here.


def home(req):
    return render(req, 'home.html')


def index(req):
    return render(req, 'Index.html')


def cart(req):
    return render(req, 'cart1.html')


def product(req, product_id=None):
    if product_id is not None:
        context = {
            'product_id': product_id
        }
        return render(req, 'ProductDetail.html', context=context)
    return render(req, 'ProductPage.html')


def signup(req):
    if req.user.is_authenticated:
        return render(req, "Login_RegPage.html", context={'loggedin': True})
    if req.method == 'POST':
        try:
            username = req.POST.get("username")
            email = req.POST.get("email")
            passwd2 = req.POST.get('psswd2')
            passwd1 = req.POST.get('psswd1')
            if passwd1 == None:
                raise "erroe"
            try:
                user = User.objects.get(email=email)
                context = {'message': {
                    'failed': True, "reason": "This Email is already exists."}}
                return render(req, "Login_RegPage.html", context=context)
            except:
                pass
            try:
                user = User.objects.get(username=username)
                context = {'message': {
                    'failed': True, "reason": "This username is already taken."}}
                return render(req, "Login_RegPage.html", context)
            except:
                pass
            if (passwd1 == passwd2):
                user = User.objects.create_user(
                    username=username, email=email, password=passwd2)
                n1 = Customer(user=user)
                n1.save()
                login(req, user)
                # print("login Success")

                # user = {'logedin': req.user.is_authenticated}
                # context = {'user': user}
                return redirect("/")
            else:
                context = {'message': {
                    'failed': True, "reason": "Password Does bot match. Please Check"}}
                return render(req, "Login_RegPage.html", context)
        except:
            username = req.POST.get("username")
            passwd = req.POST.get('password')
            try:
                user = User.objects.get(username=username)
            except:
                context = {"message":
                           {'failed': True, "reason": "This Email is not registered. Please Check"}}
                return render(req, "Login_RegPage.html", context=context)

            # authenticate(request)
            if user.check_password(passwd):
                print(user)
                login(req, user)

                return redirect("/")
            else:
                context = {'message': {'failed': True,
                                       "reason": "Wrong Password."}}
                return render(req, "Login_RegPage.html", context=context)

    return render(req, "Login_RegPage.html")


def logout_session(req):
    logout(req)
    return redirect('/')

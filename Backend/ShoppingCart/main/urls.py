from django.urls import path, include
from .views import home, index, cart

urlpatterns = [
    path('home', home),
    path('cart', cart),
    path('', index),

]

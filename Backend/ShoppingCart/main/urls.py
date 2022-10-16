from django.urls import path
from .views import index, cart, product, signup

urlpatterns = [
    path('signup', signup),
    path('product', product),
    path('cart', cart),
    path('', index),

]

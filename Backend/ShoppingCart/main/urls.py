from django.urls import path
from .views import index, cart, product, signup, logout_session

urlpatterns = [
    path('signup/', signup),
    path('signup/logout/', logout_session),
    path('product/', product),
    path('product/<int:product_id>/', product),
    path('cart', cart),
    path('', index),

]

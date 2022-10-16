from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Customer model


class Customer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(null=True)
    address = models.TextField(null=True)
    contuct_no = models.CharField(max_length=12, null=True)


# Shirt


class Product(models.Model):
    catagory = models.CharField(max_length=20)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    in_stock = models.PositiveIntegerField(default=0)


class Shirt(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(null=True)

    rating = models.IntegerField(
        choices=((1, "ONE"), (2, 'TWO'), (3, "THREE"), (4, "FOUR"), (5, "FIVE")))

    types = models.CharField(max_length=10, choices=(("formal", "formal"),
                                                     ("tshirt", "tshirt"),))

    gender = models.CharField(max_length=10, choices=(("male",    "male"),
                                                      ("female", "female")))
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
# pant


class Pants(models.Model):

    name = models.CharField(max_length=40)
    description = models.TextField()

    rating = models.IntegerField(
        choices=((1, "ONE"), (2, 'TWO'), (3, "THREE"), (4, "FOUR"), (5, "FIVE")))

    types = models.CharField(max_length=10, choices=(('jeans', "jeans"),
                                                     ('jogger', "jogger"),
                                                     ('formal', "formal"),))

    gender = models.CharField(max_length=10, choices=(("male",    "male"),
                                                      ("female", "female")))
    product = models.OneToOneField(Product, on_delete=models.CASCADE)


# women Spesific
class WomensWare (models.Model):

    name = models.CharField(max_length=40)
    description = models.TextField()

    rating = models.IntegerField(
        choices=((1, "ONE"), (2, 'TWO'), (3, "THREE"), (4, "FOUR"), (5, "FIVE")))

    types = models.CharField(max_length=10, choices=(("Kurta_set", "Kurta_set"),
                                                     ("sarri", "sarri"),
                                                     ("gown", "gown"),))
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

# Men Spesific


class MenWare (models.Model):

    name = models.CharField(max_length=40)
    description = models.TextField()

    rating = models.IntegerField(
        choices=((1, "ONE"), (2, 'TWO'), (3, "THREE"), (4, "FOUR"), (5, "FIVE")))

    types = models.CharField(max_length=10,
                             choices=(("Panjabi", "Panjabi"), ("sherwani", "sherwani")))
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

# Kids SPesific


class KidsWare(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()

    rating = models.IntegerField(
        choices=((1, "ONE"), (2, 'TWO'), (3, "THREE"), (4, "FOUR"), (5, "FIVE")))

    types = models.CharField(max_length=10,
                             choices=(("Fork", "Fork"),))

    product = models.OneToOneField(Product, on_delete=models.CASCADE)


class Goggles(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()

    rating = models.IntegerField(
        choices=((1, "ONE"), (2, 'TWO'), (3, "THREE"), (4, "FOUR"), (5, "FIVE")))
    product = models.OneToOneField(Product, on_delete=models.CASCADE)


class FootWare(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()

    rating = models.IntegerField(
        choices=((1, "ONE"), (2, 'TWO'), (3, "THREE"), (4, "FOUR"), (5, "FIVE")))

    product = models.OneToOneField(Product, on_delete=models.CASCADE)

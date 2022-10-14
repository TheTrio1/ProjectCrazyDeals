from random import choices
from secrets import choice
from django.db import models

# Create your models here.


class Product:
    name = models.CharField(max_length=40)
    description = models.TextField()
    in_stock = models.IntegerField()
    rating = models.IntegerField()

# Shirt


class Shirt(Product, models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    in_stock = models.IntegerField()
    rating = models.IntegerField(
        choices=((1, "ONE"), (2, 'TWO'), (3, "THREE"), (4, "FOUR"), (5, "FIVE")))

    types = models.CharField(max_length=10, choices=(("formal", "formal"),
                                                     ("tshirt", "tshirt"),))

    gender = models.CharField(max_length=10, choices=(("male",    "male"),
                                                      ("female", "female")))

# pant


class Pants(Product, models.Model):
    class Types(models.TextChoices):
        jeans = "jeans"
        jogger = "jogger"
        formal = "formal"

    class Gender(models.TextChoices):
        male = "male"
        female = "female"


class WomensWare (Product, models.Model):
    class Types(models.TextChoices):
        Kurta_set = "Kurta_set"
        sarri = "sarri"
        gown = "gown"


class MenWare (Product, models.Model):
    class Types(models.TextChoices):
        Panjabi = "Panjabi"
        sherwani = "sherwani"


class KidsWare(Product, models.Model):
    class Types(models.TextChoices):
        frock = "frock"


class Goggles(Product, models.Model):
    pass


class FootWare(Product, models.Model):
    pass

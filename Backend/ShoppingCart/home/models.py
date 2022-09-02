from django.db import models


class Product(models.Model):
    def __init__(self: _Self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        productID = models.CharField(max_length=10)
        price = models.DecimalField()
        modelName = models.CharField(max_length=10)
        catagory = models.CharField(max_length=10)
        description = models.TextField()
        image = models.ImageField()
        # rating

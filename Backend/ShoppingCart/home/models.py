from django.db import models


class Product(models.Model):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.productID = models.CharField(max_length=10)
        self.price = models.DecimalField()
        self.modelName = models.CharField(max_length=10)
        self.catagory = models.CharField(max_length=10)
        self.description = models.TextField()
        self.image = models.ImageField()
        # rating


class User (models.Model):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

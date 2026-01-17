from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200, unique=True)
    quantity = models.IntegerField(default=0)
    low_stock = models.IntegerField(default=5)

    def __str__(self):
        return self.name

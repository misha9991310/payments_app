from django.db import models
from django.core import validators
# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=70, verbose_name='Product Name')
    description = models.TextField(max_length=800,verbose_name='Description')
    price = models.DecimalField(max_digits=7, decimal_places=2)


    def __str__(self):
        return self.name

    def get_display_price(self):
        return f"{self.price:.2f}"

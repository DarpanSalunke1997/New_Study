from django.db import models

# Create your models here.
class Cart(models.Model):
    prod_name = models.CharField(max_length=100)
    prod_detail = models.CharField(max_length=100)
    prod_qty = models.PositiveIntegerField(default=0)
    prod_price = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.prod_name
    
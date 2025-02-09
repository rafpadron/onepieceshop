from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.TextField(max_length=300, verbose_name="Descripción")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    stock = models.PositiveIntegerField(default=True, verbose_name="Stock")
    photo = models.ImageField(upload_to='products', verbose_name="Foto", blank=True, null=True)
    
    def __str__(self):
        return self.name
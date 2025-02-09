from typing import Required
from django import forms
from django.urls import reverse_lazy
from .models import Product

class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, label="Nombre")
    description = forms.CharField(max_length=300, label="Descripción")
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="Precio")
    stock = forms.BooleanField(initial=True, label="Stock", required=False)
    photo = forms.ImageField(label="Foto", required=False)
    
    def save(self):
        Product.objects.create(
            name = self.cleaned_data['name'],
            description = self.cleaned_data['description'],
            price = self.cleaned_data['price'],
            stock = self.cleaned_data['stock'],
            photo = self.cleaned_data['photo']
        )
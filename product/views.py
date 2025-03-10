from django.shortcuts import render
from django.views import generic
from rest_framework.views import APIView
from rest_framework.response import Response

from .forms import ProductForm
from .serializers import ProductSerializer
from django.urls import reverse_lazy
from .models import Product
# Create your views here.
class ProductFormView(generic.FormView):
    template_name = 'products/add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('add_product')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ProductListView(generic.ListView):    
    model = Product
    template_name = 'products/list_product.html'
    context_object_name = 'products'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class ProductListAPI(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
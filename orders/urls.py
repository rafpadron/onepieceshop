from django.urls import path
from .views import MyOrderView, CreateOrderProductView

urlpatterns = [
    path('ordenes/', MyOrderView.as_view(), name='ordenes'),
    path('agregar-producto',  CreateOrderProductView.as_view(), name='add-products')
]

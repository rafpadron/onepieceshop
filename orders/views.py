from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Order, OrderProduct
from .forms import OrderProductForm
# Create your views here.
class MyOrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'orders/my_order.html'
    context_object_name = 'order'
    
    def get_object(self , queryset=None):
        return Order.objects.filter(is_active=True, user= self.request.user).first()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_products'] = OrderProduct.objects.filter(order=self.object)
        return context
    
class CreateOrderProductView(LoginRequiredMixin, CreateView):
    template_name = "orders/create_order_product.html"
    form_class = OrderProductForm
    success_url = reverse_lazy('ordenes')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = Order.objects.filter(
            is_active=True,
            user=self.request.user
        ).first()
        return context
    
    def form_valid(self, form):
        order, _ = Order.objects.get_or_create(
            is_active=True,
            user=self.request.user
        )
        form.instance.order = order
        form.instance.quantity = 1
        form.save()
        return super().form_valid(form)
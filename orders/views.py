from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Orders
from .forms import OrdersForm  # Assumindo que você criará um formulário para Orders

class OrdersListView(LoginRequiredMixin, ListView):
    model = Orders
    template_name = 'orders_list.html'
    context_object_name = 'orders'

class OrdersCreateView(LoginRequiredMixin, CreateView):
    model = Orders
    template_name = 'orders_create.html'
    form_class = OrdersForm
    success_url = reverse_lazy('orders_list')  # Nome da URL para redirecionar após a criação

class OrdersUpdateView(LoginRequiredMixin, UpdateView):
    model = Orders
    template_name = 'orders/order_.update.html'
    form_class = OrdersForm
    success_url = reverse_lazy('orders_list')  # Nome da URL para redirecionar após a atualização

class OrdersDeleteView(LoginRequiredMixin, DeleteView):
    model = Orders
    template_name = 'orders_delete.html'
    success_url = reverse_lazy('orders_list')  

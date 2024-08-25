from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Orders
from .forms import OrdersForm  # Assumindo que você criará um formulário para Orders

class OrdersListView(ListView):
    model = Orders
    template_name = 'orders_list.html'
    context_object_name = 'orders'

class OrdersCreateView(CreateView):
    model = Orders
    template_name = 'orders_create.html'
    form_class = OrdersForm
    success_url = reverse_lazy('orders_list')  # Nome da URL para redirecionar após a criação

class OrdersUpdateView(UpdateView):
    model = Orders
    template_name = 'orders/order_form.html'
    form_class = OrdersForm
    success_url = reverse_lazy('orders_list')  # Nome da URL para redirecionar após a atualização

class OrdersDeleteView(DeleteView):
    model = Orders
    template_name = 'orders_delete.html'
    success_url = reverse_lazy('orders_list')  # Nome da URL para redirecionar após a exclusão

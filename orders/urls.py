from django.urls import path
from .views import OrdersListView, OrdersCreateView, OrdersUpdateView, OrdersDeleteView

urlpatterns = [
    path('orders/list/', OrdersListView.as_view(), name='orders_list'),
    path('orders/create/', OrdersCreateView.as_view(), name='orders_create'),
    path('orders/<int:pk>/update/', OrdersUpdateView.as_view(), name='orders_update'),
    path('orders/<int:pk>/delete/', OrdersDeleteView.as_view(), name='orders_delete'),
    
]

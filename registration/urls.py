from django.urls import path
from . import views


urlpatterns = [
    path('registration/list/', views.RegistrationListView.as_view(), name='registration_list'),
    path('registration/create/', views.RegistrationCreateView.as_view(), name='registration_create'),
    path('registration/<int:pk>/detail/', views.RegistrationDetailView.as_view(), name='registration_detail'),
    path('registration/<int:pk>/update/', views.RegistrationUpdateView.as_view(), name='registration_update'),
    path('registration/<int:pk>/delete/', views.RegistrationDeleteView.as_view(), name='registration_delete'),
    
]

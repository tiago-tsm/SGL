from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms

class RegistrationListView(LoginRequiredMixin, ListView):
    model = models.CustomerRegistration
    template_name = 'registration_list.html'
    context_object_name = 'registration'
    paginate_by = 10
    

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset
    
    
    
class RegistrationCreateView(LoginRequiredMixin, CreateView):
        model = models.CustomerRegistration
        template_name = 'registration_create.html'
        form_class = forms.RegistrationForm
        success_url = reverse_lazy('registration_list')
        
        
        
class RegistrationDetailView(LoginRequiredMixin, DetailView):
    model = models.CustomerRegistration
    template_name = 'registration_detail.html'
    
    
    
class RegistrationUpdateView(LoginRequiredMixin, UpdateView):
    model = models.CustomerRegistration
    template_name = 'registration_update.html'
    form_class = forms.RegistrationForm
    success_url = reverse_lazy('registration_list')
   


class RegistrationDeleteView(LoginRequiredMixin, DeleteView):
    model = models.CustomerRegistration
    template_name = 'registration_delete.html'
    success_url = reverse_lazy('registration_list')
 
    
        



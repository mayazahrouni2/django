from django.shortcuts import render
from participantApp.models import Participant
from django.views.generic import CreateView,LoginView,LogoutView
from django.urls import reverse_lazy,reverse

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    def get_success_url(self):
        return reverse('conferance_list')
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
   
class UserCreateView(CreateView):
    model = Participant
    form_class = ParticipantCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')  
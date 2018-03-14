from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import RedirectView
from django.contrib.auth import logout
from .forms import CustomUserCreationForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class LogoutView(RedirectView):
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)

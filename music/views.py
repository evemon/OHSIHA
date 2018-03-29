from django.views import generic
from django.views.generic import RedirectView
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout #authenticate checks that user exists
from django.views.generic import View
from .models import Album
from .forms import UserForm


class IndexView(generic.ListView):
    #template_name = 'home.html'
    template_name = 'index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailsView(generic.DetailView):
    model = Album
    template_name = 'details.html'

class CreateNew(CreateView):
    model = Album
    fields = ['artist', 'title', 'genre']

class Update(UpdateView):
    model = Album
    fields = ['artist', 'title', 'genre']

class Delete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

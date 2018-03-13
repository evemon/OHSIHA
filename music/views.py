from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Album

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailsView(generic.DetailView):
    model = Album
    template_name = 'music/details.html'

class CreateNew(CreateView):
    model = Album
    fields = ['artist', 'title', 'genre']

class Update(UpdateView):
    model = Album
    fields = ['artist', 'title', 'genre']

class Delete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

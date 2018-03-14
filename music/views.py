from django.views import generic
from django.views.generic import TemplateView
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

class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration.html'

    #displays blank form -> none. Users will fill up the data
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # after uset push submit, not empty anymore
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            #creates the form nbutr not saving it to the db yet
            user = form.save(commit=False)

            #cleaned metadata
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            #saves to db
            user.save()

            #checks that credentials are in databse
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    #user logged in to website
                    login(request, user)
                    return redirect('music:index')
        return render(request, self.template_name, {'form': form})

class UserLogin(View):
    #form_class = UserLogin
    template_name = 'music/login.html'
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                #user logged in to website
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, "music:index")

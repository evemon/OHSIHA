from django.http import Http404
from django.shortcuts import render
from .models import Album

#collects all albums to the Music-page
def index(request):
    all_albums = Album.objects.all()
    templateInfo = {
        'all_albums': all_albums,
    }
    return render(request, 'music/index.html', templateInfo)

def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request, 'music/details.html', {'album': album})

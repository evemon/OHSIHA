from django.http import HttpResponse
from django.template import loader
from .models import Album

#collects all albums to the Music-page
def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    templateInfo = {
        'all_albums': all_albums,
    }
    return HttpResponse(template.render(templateInfo, request))

def detail(request, album_id):
    return HttpResponse("<h2>Album details for album id: " + str(album_id) + "</h2>")

from django.http import Http404
from django.shortcuts import render
from .models import Album, Song

#collects all albums to the Music-page
def index(request):
    all_albums = Album.objects.all()
    templateInfo = {
        'all_albums': all_albums,
    }
    return render(request, 'music/index.html', templateInfo)

def details(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request, 'music/details.html', {'album': album})


#function for marking song favorite
def favorite(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Song does not exist")
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, song.DoesNotExist):
        return render(request, 'music/details.html', {
            'album': album,
            'err_message': "You didn't select valid song",
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/details.html', {'album': album})

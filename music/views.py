from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Music Page</h1>")

def detail(request, album_id):
    return HttpResponse("<h2>Album details for album id: " + str(album_id) + "</h2>")

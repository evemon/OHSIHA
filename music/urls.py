
from django.conf.urls import include, url
from . import views
from django.contrib.auth.views import logout

app_name = 'music'

urlpatterns = [
    #/music
    url(r'^', views.HomeView.as_view(), name='home'),


    #album details
    url(r'^(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name='details'),
    #music/album/add
    url(r'album/add/$', views.CreateNew.as_view(), name='album-add'),
    #music/album/1/
    url(r'album/(?P<pk>[0-9]+)/$', views.Update.as_view(), name='album-update'),
    #music/album/1/delete
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.Delete.as_view(), name='album-delete'),
]

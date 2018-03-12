
from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    #/music
    url(r'^$', views.IndexView.as_view(), name='index'),

    #/music/"album-id"
    url(r'^(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name='details'),
    #music/album/add
    url(r'album/add/$', views.CreateNew.as_view(), name='album-add'),
]

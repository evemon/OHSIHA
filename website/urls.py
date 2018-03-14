
from django.contrib import admin
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^music/', include('music.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^users/', include('django.contrib.auth.urls')),
    #url(r'^login/$', auth_views.login, name='login'),
    #url(r'^logout/$', auth_views.login, name='logout')
]

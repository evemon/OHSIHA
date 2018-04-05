
from django.contrib import admin
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    #url('', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^music/', include('music.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^users/', include('django.contrib.auth.urls')),
    url(r'^recipes/', include('recipes.urls')),
]

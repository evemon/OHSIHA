from django.views import generic
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

from django.views import generic
from django.shortcuts import render
from django.views.generic import RedirectView
#from rest_framework.views import APIView
import json
from django.conf import settings
import requests



def recipesView(request):
    #dish = self.cleaned_data
    parseData = []
    #parseData = requests.get("http://www.recipepuppy.com/api/?q=" + dish)

    if 'dish' in request.GET:

        dish = request.GET['dish']

        recipes = requests.get('http://www.recipepuppy.com/api/?q=' + dish)
        recipesjson = recipes.json()

        for item in recipesjson['results']:
            recipeData = {}
            recipeData['title'] = item['title']
            recipeData['href'] = item['href']
            recipeData['ingredients'] = item['ingredients']
            recipeData['thumbnail'] = item['thumbnail']
            parseData.append(recipeData)

    return render(request, 'recipes.html', {
        'item': parseData
    })

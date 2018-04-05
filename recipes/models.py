from django.db import models
from django.urls import reverse


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    href = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=200)
    thumbnail = models.CharField(max_length=200)

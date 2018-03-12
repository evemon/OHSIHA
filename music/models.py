from django.db import models
from django.urls import reverse


class Album(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('music:details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title + ' - ' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

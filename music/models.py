from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title + ' - ' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    title = models.CharField(max_length=250)

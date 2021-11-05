from django.db import models
import datetime

#Model for Albums displayed at List Level
class Album(models.Model):
    created_at = datetime.datetime.now
    album_title = models.CharField(max_length=255)
    album_artist = models.CharField(max_length=255)
    album_labels = models.CharField(max_length=255, null=True, blank=True)
    album_tracks = models.IntegerField()

    def __str__(self):
        return self.name
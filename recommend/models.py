from django.db import models
from django.contrib.auth.models import User


class Album(models.Model):
    title = models.CharField(null=False, max_length=20)
    logo = models.TextField(null=False)
    likes = models.IntegerField(default=0)
    watched = models.IntegerField(default=0)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='album_created')

    def __str__(self):
        return self.title


class Song(models.Model):
    video_id = models.CharField(null=False, max_length=20)
    song_title = models.CharField(null=True, max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='song_related')

    def __str__(self):
        return self.song_title.encode('utf-8')

    class Meta:
        unique_together = ('video_id', 'album',)



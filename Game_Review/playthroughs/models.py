from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from game.models import Game
from embed_video.fields import EmbedVideoField


# Create your models here.
class playthroughs(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    videofile = models.FileField(upload_to='videos/', null=True, verbose_name="")

    def get_absolute_url(self):
        return reverse('playthrough-detail', kwargs={'pk':self.pk})
    #video = EmbedVideoField()



#class Video(models.Model):
    #name = models.CharField(max_length=500)
    #videofile = models.FileField(upload_to='videos/', null=True, verbose_name="")
    #video_url = models.CharField(max_length=100)


class Playthrough_Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    on_playthrough = models.ForeignKey(playthroughs, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.game.title + "\n" + self.videofile

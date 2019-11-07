from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class playthroughs(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    game_id = models.IntegerField()
    title = models.CharField(max_length=100)
    game_reviewed = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    
    
class Video(models.Model):
    name = models.CharField(max_length=500)
    videofile = models.FileField(upload_to='videos/', null=True, verbose_name="")

class Playthrough_Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    on_playthrough = models.ForeignKey(playthroughs, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.gameName + "\n" + self.name + "\n" + self.videofile

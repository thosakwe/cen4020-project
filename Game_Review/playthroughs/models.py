from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class playthroughs(models.Model):
    gameName = models.CharField(max_length=100)
    playthroughTitle = models.CharField(max_length=100)
    playDescription = models.TextField()

class Playthrough_Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    on_playthrough = models.ForeignKey(playthroughs, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.gameName
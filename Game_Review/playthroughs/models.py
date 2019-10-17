from django.db import models

# Create your models here.
class playthroughs(models.Model):
    gameName = models.CharField(max_length=100)
    playthroughTitle = models.CharField(max_length=100)
    playDescription = models.TextField()


    def __str__(self):
        return self.gameName
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from game.models import Game
from embed_video.fields import EmbedVideoField
from math import floor


# Create your models here.
class Guidebook(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    pdf_file = models.FileField(upload_to='videos/', null=True, verbose_name="")

    def get_absolute_url(self):
        return reverse('guidebook-detail', kwargs={'pk':self.pk})

    def get_likes(self):
        return self.guidebookvote_set.filter(vote=1).count()

    def get_dislikes(self):
        return self.guidebookvote_set.filter(vote=-1).count()

    def get_average(self):
        if not self.get_dislikes():
            val = 100
        else:
            val = (self.get_likes() * 100) / self.get_dislikes()
            val = round(val)
        return f"{str(val)}%"

    # def get_average(self):
    #     average = int(self.get_likes()/(self.get_likes()+self.get_dislikes()) * 100)
    #     return f"{str(average)}%"
    #video = EmbedVideoField()

class GuidebookComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    guidebook = models.ForeignKey(Guidebook, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.game.title + "\n" + self.name + "\n" + self.videofile

    class Meta:
        ordering = ['-date_posted']

    def get_likes(self):
        return self.guidebookcommentvote_set.filter(vote=1).count()

    def get_dislikes(self):
        return self.guidebookcommentvote_set.filter(vote=-1).count()

class GuidebookVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    guidebook = models.ForeignKey(Guidebook, on_delete=models.CASCADE)
    vote = models.IntegerField(default=0)
    class Meta:
       unique_together = ("user", "guidebook", "vote")

class GuidebookCommentVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(GuidebookComment, on_delete=models.CASCADE)
    vote = models.IntegerField(default=0)
    class Meta:
       unique_together = ("user", "comment", "vote")

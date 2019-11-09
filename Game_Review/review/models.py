from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from game.models import Game

# Create your models here.
class Review(models.Model):
    # On delete tells django to remove all a users post, if said user gets deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    score = models.IntegerField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('review-detail', kwargs={'pk':self.pk})

class Rating(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    on_review = models.ForeignKey(Review, on_delete=models.CASCADE)
    score = models.IntegerField()

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    on_review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
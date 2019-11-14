from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
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

    #def get_likes(self):
    #    return self.like_set.all().count()
    def get_likes(self):
        return self.reviewvote_set.filter(vote=1).count()

    def get_dislikes(self):
        return self.reviewvote_set.filter(vote=-1).count()

class Rating(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    on_review = models.ForeignKey(Review, on_delete=models.CASCADE)
    score = models.IntegerField()

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    # parent_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)
    class Meta:
        ordering = ['-date_posted']

    def get_likes(self):
        return 0

    def get_dislikes(self):
        return 0
        
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)

class ReviewVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    vote = models.IntegerField(default=0)
    class Meta:
       unique_together = ("user", "review", "vote")
"""
class ReplyTo(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    response = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="response")
"""

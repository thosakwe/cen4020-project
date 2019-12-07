from django.db import models
from django.contrib.auth.models import User
from game_review import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from review.models import Review, Comment
from playthroughs.models import playthroughs, PlaythroughComment
from guidebook.models import Guidebook, GuidebookComment

class BannedIp(models.Model):
    ip = models.TextField()

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    avatar = models.TextField()
    karma = models.IntegerField(default=0)
    banned_from_posting = models.BooleanField(default=False)

    def get_karma(self):
        reviews = Review.objects.filter(author=self.id)
        positive_content = 0
        negative_content = 0
        comment_likes = 0
        comment_dislikes = 0
        for review in reviews:
            positive_content += (review.get_likes()*5)
            negative_content += (review.get_dislikes()*3)
            comments = Comment.objects.filter(review=review.id)
            for comment in comments:
                comment_likes += comment.get_likes()
                comment_dislikes += comment.get_dislikes()

        playthroughss = playthroughs.objects.filter(author=self.id)        
        for playthrough in playthroughss:
            positive_content += (playthrough.get_likes()*5)
            negative_content += (playthrough.get_dislikes()*3)
            comments = PlaythroughComment.objects.filter(playthrough=playthrough.id)
            for comment in comments:
                comment_likes += comment.get_likes()
                comment_dislikes += comment.get_dislikes()

        guidebooks = Guidebook.objects.filter(author=self.id)
        for guidebook in guidebooks:
            positive_content += (guidebook.get_likes()*5)
            negative_content += (guidebook.get_dislikes()*3)
            comments = GuidebookComment.objects.filter(guidebook=guidebook.id)
            for comment in comments:
                comment_likes += comment.get_likes()
                comment_dislikes += comment.get_dislikes()
        content_karma = positive_content - negative_content
        comment_karma = comment_likes - comment_dislikes
        return content_karma + comment_karma

        content_karma = positive_content - negative_content
        comment_karma = comment_likes - comment_dislikes
        return content_karma + comment_karma

@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    """
    Creates and attaches a user profile once a user is created
    """
    if created:
        Profile.objects.create(user=instance)
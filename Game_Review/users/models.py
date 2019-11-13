from django.db import models
from django.contrib.auth.models import User
from game_review import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    avatar = models.TextField()

@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    """
    Creates and attaches a user profile once a user is created
    """
    if created:
        Profile.objects.create(user=instance)
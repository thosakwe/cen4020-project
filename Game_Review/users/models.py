from django.db import models
from django.contrib.auth.models import User
from game_review import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    avatar = models.TextField()
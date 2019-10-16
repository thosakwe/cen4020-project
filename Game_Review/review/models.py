from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    # On delete tells django to remove all a users post, if said user gets deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    game_reviewed = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    path = models.TextField()
    mime_type = models.TextField() # The type of file, i.e. image/jpeg
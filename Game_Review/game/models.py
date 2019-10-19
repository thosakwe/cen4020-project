from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

def game_public_url(game):
  return "/static/game_images/" + str(game.id) + ".jpg"

class Game(models.Model):
  image_path = models.TextField(max_length = 50,default='ab') # The path to the cover image, ex. "/static/games/battlefront.jpg"
  title = models.TextField(max_length = 50,default='non')
  description = models.TextField()
  cost = models.IntegerField(default=0)
  # TODO: Maybe we can add more fields here, i.e. "what company made this game?" "what genre is it?"

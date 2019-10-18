from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

def game_public_url(game):
  return "/static/game_images/" + str(game.id) + ".jpg"

# class Game(models.Model):
#   image_path = models.TextField() # The path to the cover image, ex. "/static/games/battlefront.jpg"
#   title = models.TextField()
#   description = models.TextField()

  # TODO: Maybe we can add more fields here, i.e. "what company made this game?" "what genre is it?"
class Game(models.Model):
	"""docstring for games"""
	name = models.CharField(max_length = 50,default='ab')
	title = models.TextField(max_length = 50,default='non')
	image_path = models.TextField(max_length = 50,default='ab')

#class User(models.Model):
#    firstname = models.CharField(max_length = 50)
#    lastname = models.Charfield(max_length = 50)
#    email = models.CharField(max_length = 200)
#    password = models.CharField(max_length = 200)

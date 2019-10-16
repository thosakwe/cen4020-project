# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import NewGameForm
from .models import Game, game_public_url
import os

# Create your views here.

# TODO: Only allow admins to create games
# TODO: *Should* only admins be allowed to create games?
@login_required
def new(request):
  errors = []
  if request.method == "POST":
    form = NewGameForm(request.POST, request.FILES)
    if not form.is_valid():
      errors = form.errors
    else:
      # Insert the game into the database.
      image = form.cleaned_data['image']
      title = form.cleaned_data['title']
      description = form.cleaned_data['description']
      # Validate the image
      if image.content_type != "image/jpeg":
        errors.extend(
            ["Profile pictures must be jPEG images."])
      else:
        game = Game()
        game.title = title
        game.description = title
        game.save()
        # Save the cover image.
        image_file_path = "reviews/" + game_public_url(game)
        image_dir = os.path.dirname(image_file_path)
        if not os.path.exists(image_dir):
          os.makedirs(image_dir)
        with open(image_file_path, "wb") as file:
          for chunk in image.chunks():
            file.write(chunk)
        # Redirect to the game's page.
        return redirect("/games/" + str(game.id))
  return render(request, 'Game/new_game.html', {'errors': errors})
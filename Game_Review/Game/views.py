# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from review.models import Review
from statistics import mean
from .forms import NewGameForm
from .models import Game, game_public_url
import os

# Create your views here.


def get_by_id(request, id):
    game = Game.objects.get(pk=id)
    reviews = Review.objects.filter(game_id=game.id)
    if not reviews:
        review_classes = []
    else:
        avg_review = mean([r.score for r in reviews])
        review_classes = []
        for i in range(0, avg_review):
            review_classes.append("fas fa-star")
        for i in range(avg_review, 5):
            review_classes.append("far fa-star")
    return render(request, 'Game/game.html', {'game': game, 'image_url': game_public_url(game),
                                              'review_classes': review_classes})

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
                    ["Cover images must be jPEG images."])
            else:
                game = Game()
                game.title = title
                game.description = description
                game.save()
                # Save the cover image.
                image_file_path = "review/" + game_public_url(game)
                image_dir = os.path.dirname(image_file_path)
                if not os.path.exists(image_dir):
                    os.makedirs(image_dir)
                with open(image_file_path, "wb") as file:
                    for chunk in image.chunks():
                        file.write(chunk)
                # Redirect to the game's page.
                return redirect("/games/" + str(game.id))
    return render(request, 'Game/new_game.html', {'errors': errors})

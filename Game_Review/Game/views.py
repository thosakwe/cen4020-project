# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

# TODO: Only allow admins to create games
# TODO: *Should* only admins be allowed to create games?
@login_required
def new(request):
  return render(request, 'Game/new_game.html')
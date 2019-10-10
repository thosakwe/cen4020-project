
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#


class User(models.Model):
    firstname = models.CharField(max_length = 50)
    lastname = models.Charfield(max_length = 50)
    email = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)

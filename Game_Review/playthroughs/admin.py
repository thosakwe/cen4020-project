from django.contrib import admin

# Register your models here.
from .models import playthroughs
from .models import Video

# Register your models here.
# -*- coding: utf-8 -*-
admin.site.register(playthroughs)
admin.site.register(Video)

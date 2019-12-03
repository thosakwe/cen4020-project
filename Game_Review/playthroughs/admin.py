from django.contrib import admin

# Register your models here.
from .models import playthroughs, PlaythroughVote, PlaythroughComment, PlaythroughCommentVote


# Register your models here.
# -*- coding: utf-8 -*-
admin.site.register(playthroughs)
admin.site.register(PlaythroughVote)
admin.site.register(PlaythroughComment)
admin.site.register(PlaythroughCommentVote)



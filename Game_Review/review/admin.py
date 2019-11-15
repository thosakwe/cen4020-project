from __future__ import unicode_literals

from django.contrib import admin

from .models import Review, Comment, ReviewVote

# Register your models here.
# -*- coding: utf-8 -*-
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(ReviewVote)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'on_review', 'content', 'date_posted')
    list_filter = ('date_posted')
    search_fields = ('body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
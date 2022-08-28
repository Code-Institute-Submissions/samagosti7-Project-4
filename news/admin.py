"""
        This file enables admin functionality, specifically the ability to
        unpublish and delete any existing posts or comments.
    """
from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

"""
        CREDIT--admin functionality for posts coming from blog lesson on
        https://learn.codeinstitute.net/
    """


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
        Manages admin functionality for posts
    """

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
        Manages admin functionality for comments
    """

    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """
        Comment approval--set to true so comments are approved by default.
        """
        queryset.update(approved=True)

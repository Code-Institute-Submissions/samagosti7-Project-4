"""
        This file contains both forms used for posting a new comment,
        and for creating a new news post
    """
from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    """
        Form for comment submission
    """
    class Meta:
        """
        Metadata for comment form
        """
        model = Comment
        fields = ('body',)
        labels = {'body': ""}


class PostForm(forms.ModelForm):
    """
        Form for post submission
    """
    class Meta:
        """
        Metadata for post form
        """
        model = Post
        fields = ['title', 'content']
        labels = {'title': 'Title', 'content': 'Post Content'}

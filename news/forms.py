from .models import Comment, Post
from django import forms

# Form for comment submission
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {'body': ""}

# Form for post submission
class PostForm(forms.ModelForm):
    class Meta: 
        model = Post
        fields = ['title', 'content']

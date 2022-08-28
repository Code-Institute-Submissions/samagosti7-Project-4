"""
        File containing both base models, for a post and for a comment
        """
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Assigning status definitions
STATUS = ((0, "Draft"), (1, "Published"))

"""
        CREDIT--model skeletons used from https://learn.codeinstitute.net/, in
        a mini project covering blog posts.
        """


class Post(models.Model):
    """
        Post model
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="news_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    likes = models.ManyToManyField(User, related_name="news_likes")

    class Meta:
        """
        Metadata for Post model
        """
        ordering = ['-created_on']

    def __str(self):
        return self.title

    def number_of_likes(self):
        """
        Function returning the number of likes on a post
        """
        return self.likes.count()


class Comment(models.Model):
    """
        Comment model
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="news_comment")

    class Meta:
        """
        Metadata for Comment model
        """
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'

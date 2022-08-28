"""
        File containing all views across the entirety of the news app
    """
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from .models import Post, Comment
from .forms import CommentForm, PostForm


class PostList(generic.ListView):
    """
        View for the html page listing all available posts, with
        pagination when necessary
    """

    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "post_list.html"
    paginate_by = 6


class PostDetail(View):
    """
        View for the html page loaded when a user selects an individual post
        to read
    """

    def get(self, request, slug, *args, **kwargs):
        """
        Retrieving and rendering the post
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Retrieving and rendering comments
        """

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Comment submitted successfully'
            )
        else:
            comment_form = CommentForm()
            messages.add_message(
                request,
                messages.WARNING,
                'Something went wrong. Please try again.'
            )

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):
    """
        View for the reload of the page, after the user has like it, with the
        likes button and count refelcted accordingly
    """

    def post(self, request, slug, *args, **kwargs):
        """
        Toggling between liking and unliking a post as a user and reloading
        page accordingly.
        """
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class MakePostView(View):
    """
        View for the html page and form presented when a user begins post creation
    """

    def get(self, request):
        """
        Retrieval and rendering of blank post form
        """

        post_form = PostForm()

        return render(
            request,
            "make_post.html",
            {
                "post_form": post_form,
            }
        )

    def post(self, request):
        """
        Processing submission of post form. If valid, database is updated and
        a success message is dislayed.
        """

        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            post_form.instance.author = request.user
            print(dir(post_form))
            post_form.instance.slug = slugify(post_form.instance.title)
            post = post_form.save()
            post.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Post submitted successfully'
            )
        else:
            post_form = PostForm()
            messages.add_message(
                request,
                messages.WARNING,
                'Something went wrong, please try again'
            )
        return HttpResponseRedirect(reverse('post_list'))


class EditPostView(View):
    """
        View for the html page displayed when a user chooses to edit a post.
    """

    def get(self, request, id):
        """
        Retrieval and rendering of existing form data, to be edited
        """

        queryset = Post.objects.all()
        post = get_object_or_404(queryset, id=id)

        data = {'title': post.title, 'content': post.content}
        edit_form = PostForm(initial=data)

        return render(
            request,
            "edit_post.html",
            {
                "post": post,
                "edit_form": edit_form
            }
        )

    def post(self, request, id):
        """
        Evaluation and submission of new post form after edits. If completed
        correctly, a success message is displayed
        """

        queryset = Post.objects.all()
        post = get_object_or_404(queryset, id=id)

        edit_form = PostForm(instance=post, data=request.POST)

        if edit_form.is_valid():
            post.title = edit_form.cleaned_data.get('title')
            post.content = edit_form.cleaned_data.get('content')
            post.slug = slugify(edit_form.cleaned_data.get('title'))
            post.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Post Edited.'
            )
        else:
            edit_form = PostForm()
            messages.add_message(
                request,
                messages.WARNING,
                'Edit failed, try again'
            )

        return HttpResponseRedirect(reverse('post_list'))


class DeletePostView(View):
    """
        View for the html page displayed when a user chooses to delete a post
    """

    def get(self, request, id):
        """
        Retrieval of post to be deleted
        """

        queryset = Post.objects.all()
        post = get_object_or_404(queryset, id=id)
        return render(
            request,
            "delete_post.html",
            {
                "post": post,
            }
        )

    def post(self, request, id):
        """
        Deletion of selected post, with accompanying success message.
        """

        queryset = Post.objects.all()
        post = get_object_or_404(queryset, id=id)

        post.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            'Post deleted.'
        )
        return HttpResponseRedirect(reverse('post_list'))


class DeleteCommentView(View):
    """
        View for the html page displayed when a user chooses to delete a comment
    """

    def get(self, request, id):
        """
        Retrieval of comment to be deleted
        """

        queryset = Comment.objects.all()
        comment = get_object_or_404(queryset, id=id)
        return render(
            request,
            "delete_comment.html",
            {
                "comment": comment,
            }
        )

    def post(self, request, id):
        """
        Deleting selected comment, with accompanying success message
        """

        queryset = Comment.objects.all()
        comment = get_object_or_404(queryset, id=id)
        slug = comment.post.slug

        comment.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            'Comment deleted.'
        )
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

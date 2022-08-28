from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from .models import Post, Comment
from .forms import CommentForm, PostForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "post_list.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
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
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class MakePostView(View):

    def get(self, request):

        post_form = PostForm()

        return render(
            request,
            "make_post.html",
            {
                "post_form": post_form,
            }
        )
    
    def post(self, request):

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
    def get(self, request, id):
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
    def get(self, request, id):
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
    def get(self, request, id):
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


    
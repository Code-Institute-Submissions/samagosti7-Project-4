"""
        File containing all imported urls and paths for our news app
        """
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('post_list', views.PostList.as_view(), name='post_list'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('make_post', views.MakePostView.as_view(), name='make_post'),
    path('edit_post/<int:id>/', views.EditPostView.as_view(),
         name='edit_post'),
    path('delete_post/<int:id>/', views.DeletePostView.as_view(),
         name='delete_post'),
    path('delete_comment/<int:id>/', views.DeleteCommentView.as_view(),
         name='delete_comment'),
]

from . import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('make_post', views.MakePostView.as_view(), name='make_post'),
    path('post_list', views.PostList.as_view(), name='post_list'),
]

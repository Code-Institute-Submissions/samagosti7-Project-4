from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('summernote/', include('django.summernote.urls')),
    path('', include('news.urls'), name='news.urls')
    
]

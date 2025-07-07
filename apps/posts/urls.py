from django.urls import path
from apps.posts.views import PostCreateView, PostListView

urlpatterns = [
    path('post/create/', PostCreateView.as_view(), name='create_post'),
    path('post/my/', PostListView.as_view(), name='list_post')
]

#urls de mi app de post
from django.urls import path
from .views import PostListView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
]
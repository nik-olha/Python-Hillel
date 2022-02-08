from django.urls import path
from .views import PostView, PostDetailView, PostDeleteView


urlpatterns = [
    path("posts/", PostView.as_view()),
    path("posts/<int:pk>/", PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view())
]

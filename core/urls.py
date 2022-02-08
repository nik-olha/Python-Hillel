from django.urls import path
from .views import PostView, PostDetailView, PostDeleteView, PostUpdateView, PostCreateView

app_name = "posts"
urlpatterns = [
    path("posts/", PostView.as_view(), name='list'),
    path("posts/<int:pk>/", PostDetailView.as_view(), name='detail'),
    path("posts_delete/<int:pk>/", PostDeleteView.as_view(), name='delete'),
    path("posts_update/<int:pk>/", PostUpdateView.as_view(), name='update'),
    path("posts_update/", PostCreateView.as_view(), name='create')
]

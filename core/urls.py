from django.urls import path
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .views import PostView, PostDetailView, PostDeleteView, PostUpdateView, PostCreateView

app_name = "posts"
urlpatterns = [
    path("", lambda _: HttpResponseRedirect(reverse_lazy("posts:list"))),
    path("posts/", PostView.as_view(), name='list'),
    path("posts/<int:pk>/", PostDetailView.as_view(), name='detail'),
    path("posts_delete/<int:pk>/", PostDeleteView.as_view(), name='delete'),
    path("posts_update/<int:pk>/", PostUpdateView.as_view(), name='update'),
    path("posts_create/", PostCreateView.as_view(), name='create')
]

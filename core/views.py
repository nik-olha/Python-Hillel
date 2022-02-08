# from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView

# def posts(request):
#     posts = Post.objects.all()
#     results = ", ".join([post.title for post in posts])
#     return HttpResponse(results)


class PostView(ListView):
    template_name = 'core/posts.html'
    queryset = Post.objects.all()

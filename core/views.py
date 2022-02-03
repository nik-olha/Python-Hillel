# from django.http import HttpResponse
from .models import Post, Like
from django.db.models import query
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView

# def posts(request):
#     posts = Post.objects.all()
#     results = ", ".join([post.title for post in posts])
#     return HttpResponse(results)


class PostView(ListView):
    template_name = 'core/posts.html'
    queryset = Post.objects.all()
    # context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.all()
        results = [
            (
                p, 
                p.like_set.filter(status=True).count(),
                p.like_set.filter(status=False).count()
            ) 
                for p in posts
        ]
        context['results'] = results
        return context
    
class PostDetailView(DetailView):
    queryset = Post.objects.all()
    template_name = 'core/post.html'


class PostDeleteView():
    pass

class PostUpdateView():
    pass

class PostCreateView():
    pass
from .models import Post, Like
from django.db.models import query
from django.views.generic import ListView, DetailView, DeleteView


class PostView(ListView):
    template_name = 'core/posts.html'
    queryset = Post.objects.all()

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.all()
        post = self.object

        context['likes'] = post.like_set.filter(status=True).count()
        context['dislikes'] = post.like_set.filter(status=False).count()
        return context


class PostDeleteView(DeleteView):
    model = Post
    success_url = "/"


class PostUpdateView():
    pass


class PostCreateView():
    pass

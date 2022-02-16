from .models import Post
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from .forms import PostForm
# from .forms import SignUpForm
from django.contrib.auth import get_user_model

User = get_user_model()


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
        post = self.object

        context['likes'] = post.like_set.filter(status=True).count()
        context['dislikes'] = post.like_set.filter(status=False).count()
        return context


class PostDeleteView(DeleteView):
    queryset = Post.objects.all()
    template_name = 'core/post_delete.html'
    model = Post
    success_url = reverse_lazy("posts:list")


class PostUpdateView(UpdateView):
    queryset = Post.objects.all()
    template_name = 'core/post_update.html'
    fields = ["title", "content"]
    success_url = reverse_lazy("posts:list")


class PostCreateView(CreateView):
    queryset = Post.objects.all()
    template_name = 'core/post_create.html'
    # fields = ["title", "content", "user"]
    success_url = reverse_lazy("posts:list")
    form_class = PostForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# class UserSignUpView(CreateView):
#     queryset = User.objects.all()
#     template_name = 'auth/signup.html'
#     success_url = reverse_lazy("posts:list")
#     form_class = SignUpForm
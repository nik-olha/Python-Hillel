from django import forms
from core.models import Post
from django.contrib.auth import get_user_model


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]

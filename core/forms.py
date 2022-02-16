from django import forms
from core.models import Post
from django.contrib.auth import get_user_model

# User = get_user_model()

# class SignUpForm(forms.Form):
#     username= forms.CharField()
#     firls_name = forms.CharField()
#     last_name = forms.CharField()
#     email = forms.EmailField()
#     password1 = forms.CharField()
#     password2 = forms.CharField()
 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]

    # def save(self, commit=True):
    #     post = super().save(commit=False)
    #     # setattr(post, 'user', User.objects.first())
    #     post.user = User.objects.first()
    #     if commit:
    #         post.save()
    #     return post

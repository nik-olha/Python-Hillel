from django import forms
# from core.models import Post
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "password1", "password2", "sex", "phone_number"]


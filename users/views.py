from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from .forms import  UserSignUpForm
User = get_user_model()



def users(requests):
    users = get_user_model().objects.all()
    results = ", ".join([user.username for user in users])
    return HttpResponse(results)


class SignUpView(CreateView):
    queryset = get_user_model().objects.all()
    template_name = 'registration/signup.html'
    success_url = reverse_lazy("login")
    form_class  = UserSignUpForm
   

from django.contrib.auth import get_user_model
from django.http import HttpResponse

User = get_user_model()


def users(requests):
    users = User.objects.all()
    results = ", ".join([user.username for user in users])
    return HttpResponse(results)

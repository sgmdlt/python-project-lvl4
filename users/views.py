from django.views.generic import ListView

from .models import User


class UsersView(ListView):

    template = 'users.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.order_by('-created_at')

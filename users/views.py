from django.views.generic import ListView
from users.models import User


class UsersView(ListView):

    context_object_name = 'users_list'
    template_name = 'users/users.html'
    model = User

    def get_queryset(self):
        return User.objects.all().order_by('-created_at')

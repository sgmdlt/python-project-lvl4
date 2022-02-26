from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from users.forms import CustomUserCreationForm
from users.models import CustomUser


class UsersView(ListView):

    context_object_name = 'users_list'
    template_name = 'users/users.html'
    model = CustomUser

    def get_context_data(self, **kwargs):  # noqa:WPS612
        return super().get_context_data(**kwargs)


class RegistrationView(CreateView):
    """User registration view."""

    form_class = CustomUserCreationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:home')

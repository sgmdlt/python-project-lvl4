from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from users.forms import CustomUserCreationForm
from users.models import CustomUser


class UsersView(ListView):

    context_object_name = "users_list"
    template_name = "users/index.html"
    model = CustomUser

    def get_context_data(self, **kwargs):  # noqa:WPS612
        return super().get_context_data(**kwargs)


class RegistrationView(CreateView):

    form_class = CustomUserCreationForm
    template_name = "users/create.html"
    success_url = reverse_lazy("users:index")

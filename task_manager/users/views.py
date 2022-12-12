from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from task_manager.users.forms import UserForm
from task_manager.users.models import User

from .mixins import UserHasPermissionMixin


class IndexView(ListView):
    template_name = "users/index.html"
    model = User


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = "users/create.html"
    success_url = reverse_lazy("login")
    success_message = _("User successfully created")


class UserUpdateView(UserHasPermissionMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = "users/update.html"
    success_url = reverse_lazy("users:index")
    success_message = _("User successfully updated")


class UserDeleteView(UserHasPermissionMixin, SuccessMessageMixin, DeleteView):
    model = User
    success_url = reverse_lazy("users:index")
    template_name = "users/delete.html"
    success_message = _("User successfully deleted")

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
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
    success_message = _("User successfully registered")


class UserUpdateView(UserHasPermissionMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = "users/update.html"
    success_url = reverse_lazy("users:index")
    success_message = _("User successfully updated")


class UserDeleteView(UserHasPermissionMixin, DeleteView):
    model = User
    success_url = reverse_lazy("users:index")
    template_name = "users/delete.html"

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
        except ProtectedError:
            messages.error(
                self.request,
                _("Cannot delete a user because he is being used"),
            )
        else:
            messages.success(
                self.request,
                _("User successfully deleted"),
            )
        return HttpResponseRedirect(success_url)

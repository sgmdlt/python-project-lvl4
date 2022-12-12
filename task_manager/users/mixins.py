from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls.base import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _


class UserHasPermissionMixin(LoginRequiredMixin, UserPassesTestMixin):

    login_url = reverse_lazy("login")

    def test_func(self):
        return self.get_object() == self.request.user

    def handle_no_permission(self):
        messages.error(
            self.request, _("You have no rights to change or delete another user.")
        )
        return redirect("users:index")

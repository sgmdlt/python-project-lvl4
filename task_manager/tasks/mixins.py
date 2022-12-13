from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.urls.base import reverse_lazy
from django.utils.translation import gettext as _


class CheckTaskCreator(UserPassesTestMixin):

    login_url = reverse_lazy("login")

    def test_func(self):
        return self.get_object().creator == self.request.user

    def handle_no_permission(self):
        messages.error(
            self.request,
            _("Task can be deleted only by its author"),
        )
        return redirect("tasks:index")

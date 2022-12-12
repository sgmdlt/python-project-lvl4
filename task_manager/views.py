from django.views.generic.base import TemplateView

from django.contrib.auth.views import (
    LoginView as DjangoLoginView,
    LogoutView as DjangoLogoutView,
)
from django.urls.base import reverse_lazy
from django.utils.translation import gettext as _
from django.contrib.messages.views import SuccessMessageMixin


class IndexView(TemplateView):

    template_name = "index.html"


class LoginView(SuccessMessageMixin, DjangoLoginView):
    success_message = _("You are logged in")
    template_name = "login.html"

    def get_success_url(self):
        return reverse_lazy("index")


class LogoutView(SuccessMessageMixin, DjangoLogoutView):
    success_message = _("You are logged out")
    next_page = reverse_lazy("index")

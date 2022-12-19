from django.contrib import messages
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.contrib.auth.views import LogoutView as DjangoLogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls.base import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic.base import TemplateView


class IndexView(TemplateView):

    template_name = "index.html"


class LoginView(SuccessMessageMixin, DjangoLoginView):
    success_message = _("You are logged in")
    template_name = "login.html"

    def get_success_url(self):
        return reverse_lazy("index")


class LogoutView(DjangoLogoutView):
    next_page = reverse_lazy("index")

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _("You are logged out"))
        return super().dispatch(request, *args, **kwargs)

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import StatusForm
from .models import Status


class IndexView(LoginRequiredMixin, ListView):
    template_name = "statuses/index.html"
    model = Status


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = "statuses/create.html"
    success_url = reverse_lazy("statuses:index")
    success_message = _("Status successfully created")


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = "statuses/update.html"
    success_url = reverse_lazy("statuses:index")
    success_message = _("Status successfully updated")


class StatusDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Status
    success_url = reverse_lazy("statuses:index")
    success_message = _("Status successfully deleted")
    template_name = "statuses/delete.html"

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
        except ProtectedError:
            messages.error(
                self.request,
                _("Status is used by task"),
            )
        return HttpResponseRedirect(success_url)

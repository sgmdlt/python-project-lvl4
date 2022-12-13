from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import TaskForm
from .mixins import CheckTaskCreator
from .models import Task


class IndexView(LoginRequiredMixin, ListView):
    template_name = "tasks/index.html"
    model = Task


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "tasks/detail.html"


class TaskCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/create.html"
    success_url = reverse_lazy("tasks:index")
    success_message = _("Task successfully created")

    def form_valid(self, form):
        form.instance.creator = self.request.user

        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/update.html"
    success_url = reverse_lazy("tasks:index")
    success_message = _("Task successfully updated")


class TaskDeleteView(  # noqa: WPS215
    LoginRequiredMixin,
    SuccessMessageMixin,
    CheckTaskCreator,
    DeleteView,
):
    model = Task
    success_url = reverse_lazy("tasks:index")
    success_message = _("Task successfully deleted")
    template_name = "tasks/delete.html"

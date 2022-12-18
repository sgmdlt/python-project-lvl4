from django.forms import ModelForm

from .models import Task


class TaskForm(ModelForm):
    """Site user creation form."""

    class Meta:  # noqa: WPS306
        model = Task
        fields = ["name", "description", "status", "executor", "labels"]

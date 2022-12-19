import django_filters
from django.forms import CheckboxInput
from django.utils.translation import gettext as _
from task_manager.labels.models import Label

from .models import Task


class TaskFilter(django_filters.FilterSet):
    self_tasks = django_filters.BooleanFilter(
        field_name="creator",
        method="get_self_tasks",
        label=_("Only own tasks"),
        widget=CheckboxInput,
    )
    label = django_filters.ModelChoiceFilter(
        field_name="labels",
        label=_("Label"),
        queryset=Label.objects.all(),
    )

    def get_self_tasks(self, queryset, field_name, value):  # noqa: WPS110, WPS615
        if value:
            return queryset.filter(creator=self.request.user)
        return queryset

    class Meta:  # noqa: WPS306
        model = Task
        fields = ["status", "executor", "label", "self_tasks"]

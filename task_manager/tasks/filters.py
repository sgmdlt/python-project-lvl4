import django_filters
from django.utils.translation import gettext as _

from .models import Task
from task_manager.labels.models import Label


class TaskFilter(django_filters.FilterSet):
    self_tasks = django_filters.BooleanFilter(
        field_name="creator",
        method="get_self_tasks",
        label=_("Only own tasks"),
    )
    label = django_filters.ModelChoiceFilter(
        field_name="labels",
        label=_("Label"),
        queryset=Label.objects.all(),
    )

    def get_self_tasks(self, queryset, field_name, value):
        if value:
            return queryset.filter(creator=self.request.user)
        return queryset

    class Meta:
        model = Task
        fields = ["status", "executor", "label", "self_tasks"]

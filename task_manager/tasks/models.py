from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from task_manager.labels.models import Label
from task_manager.statuses.models import Status

MAX_LENGTH = 50


class Task(models.Model):
    name = models.CharField(_("name"), max_length=MAX_LENGTH)
    description = models.TextField(_("description"))
    status = models.ForeignKey(
        Status,
        verbose_name=_("status"),
        on_delete=models.PROTECT,
        null=True,
    )
    creator = models.ForeignKey(
        get_user_model(),
        verbose_name=_("creator"),
        on_delete=models.PROTECT,
        related_name="creator",
    )
    executor = models.ForeignKey(
        get_user_model(),
        verbose_name=_("executor"),
        on_delete=models.PROTECT,
        related_name="executor",
    )
    created_at = models.DateTimeField(_("created at"), auto_now=True)
    labels = models.ManyToManyField(
        Label,
        verbose_name=_("labels"),
        blank=True,
        related_name="labels",
        through="TaskLabel",
    )

    def __str__(self):
        return self.name


class TaskLabel(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.RESTRICT)

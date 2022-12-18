from django.contrib.auth import get_user_model
from django.db import models
from task_manager.statuses.models import Status

MAX_LENGTH = 50


class Task(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True)
    creator = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name="creator",
    )
    executor = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        related_name="executor",
    )
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
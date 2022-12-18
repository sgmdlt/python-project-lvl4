from django.db import models

MAX_LENGTH = 50


class Label(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

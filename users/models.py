from django.db import models

NAME_LENGHT = 100


class User(models.Model):
    first_name = models.CharField(max_length=NAME_LENGHT, null=True)
    last_name = models.CharField(max_length=NAME_LENGHT)
    username = models.CharField(max_length=NAME_LENGHT, null=True)
    created_at = models.DateTimeField('date created', auto_now_add=True)

    def __str__(self):
        """Return text representation."""
        return '{0} {1}'.format(self.first_name, self.last_name)

    @property
    def time(self):
        return self.created_at.strftime("%d.%m.%Y %H:%M")

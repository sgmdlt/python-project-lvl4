from django.db import models

NAME_LENGHT = 100


class User(models.Model):
    first_name = models.CharField(max_length=NAME_LENGHT, null=True)
    last_name = models.CharField(max_length=NAME_LENGHT)
    username = models.CharField(max_length=NAME_LENGHT, null=True)
    created_at = models.DateTimeField('date created')

    def __str__(self):
        """Return text representation."""
        return self.question_text

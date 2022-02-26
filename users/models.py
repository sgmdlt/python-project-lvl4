from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

MAX_LENGTH = 255


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=MAX_LENGTH)
    username = models.CharField(max_length=MAX_LENGTH, unique=True)

    USERNAME_FIELD = 'username'  # noqa:WPS115 upper-case constant in a class

    class Meta(object):
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        """Return text representation."""
        return '{0} {1}'.format(self.first_name, self.last_name)

    @property
    def time(self):
        return self.date_joined.strftime("%d.%m.%Y %H:%M")

    def get_absolute_url(self):
        """Return the url of an instance."""
        return reverse('user', kwargs={'id': self.id})

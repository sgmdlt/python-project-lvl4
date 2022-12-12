from django.contrib.auth.models import AbstractUser
from django.urls import reverse

MAX_LENGTH = 255


class User(AbstractUser):
    def __str__(self):
        return self.get_full_name()

    def get_absolute_url(self):
        return reverse("users:index")

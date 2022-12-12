from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserForm(UserCreationForm):
    """Site user creation form."""

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name")

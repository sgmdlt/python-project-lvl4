from django.forms import ModelForm

from .models import Status


class StatusForm(ModelForm):
    """Site user creation form."""

    class Meta:  # noqa: WPS306
        model = Status
        fields = ["name"]

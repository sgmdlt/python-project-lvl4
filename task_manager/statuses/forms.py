from django.forms import ModelForm

from .models import Status


class StatusForm(ModelForm):
    """Site user creation form."""

    class Meta(ModelForm.Meta):
        model = Status
        fields = ["name"]

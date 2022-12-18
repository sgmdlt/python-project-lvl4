from django.forms import ModelForm

from .models import Label


class LabelForm(ModelForm):
    """Site user creation form."""

    class Meta:  # noqa: WPS306
        model = Label
        fields = ["name"]

from django.conf import settings


def settings_processor(request):
    """Set settings processor."""
    return {
        'settings': settings,
    }

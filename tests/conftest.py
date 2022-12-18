import json
from pathlib import Path

import pytest


@pytest.fixture(autouse=True)
def whitenoise_autorefresh(settings):
    """
    Get rid of whitenoise "No directory at" warning, as it's not helpful when running tests.

    Related:
        - https://github.com/evansd/whitenoise/issues/215
        - https://github.com/evansd/whitenoise/issues/191
        - https://github.com/evansd/whitenoise/commit/4204494d44213f7a51229de8bc224cf6d84c01eb
    """
    settings.WHITENOISE_AUTOREFRESH = True


def get_fixture(filename):
    current_dir = Path(__file__).absolute().parent
    return current_dir / "fixtures" / filename


@pytest.fixture
def test_data(scope="session"):
    return json.loads(open(get_fixture("test_data.json")).read())

import json
from pathlib import Path

import pytest


def get_fixture(filename):
    current_dir = Path(__file__).absolute().parent
    return current_dir / "fixtures" / filename


@pytest.fixture
def test_data(scope="session"):
    return json.loads(open(get_fixture("test_data.json")).read())

import pytest
from django.urls import reverse
from task_manager.statuses.models import Status
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import ProtectedError
from django.core.management import call_command
from conftest import get_fixture


@pytest.fixture(scope="module")
def django_db_setup(django_db_setup, django_db_blocker, request):
    def clear_db():
        with django_db_blocker.unblock():
            call_command("flush", "--noinput")

    request.addfinalizer(clear_db)
    with django_db_blocker.unblock():
        call_command("loaddata", get_fixture("users.json"))
        call_command("loaddata", get_fixture("statuses.json"))


@pytest.fixture()
def client(client, test_data):
    exist_user = test_data["users"]["existing"]
    client.login(
        username=exist_user["username"],
        password=exist_user["password"],
    )
    yield client


@pytest.mark.django_db
def test_statuses_page(client):
    url = reverse("statuses:index")
    response = client.get(url)

    assert len(response.context["status_list"]) == 3
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_status(client, test_data):
    new_status = test_data["statuses"]["new"]
    url = reverse("statuses:create")
    client.post(url, new_status)

    created_status = Status.objects.get(name=new_status["name"])
    assert created_status.name == new_status["name"]


@pytest.mark.django_db
def test_update_status(client, test_data):
    status = test_data["statuses"]["existing"]
    new_status = test_data["statuses"]["new"]

    existed_status = Status.objects.get(name=status["name"])

    url = reverse("statuses:update", args=[existed_status.pk])
    client.post(url, new_status)

    updated_status = Status.objects.get(name=new_status["name"])
    assert updated_status.name == new_status["name"]


@pytest.mark.django_db
def test_delete_status(client, test_data):
    status = test_data["statuses"]["existing"]
    existed_status = Status.objects.get(name=status["name"])

    url = reverse("statuses:delete", args=[existed_status.pk])
    client.post(url)

    with pytest.raises(ObjectDoesNotExist):
        assert Status.objects.get(name=status["name"])

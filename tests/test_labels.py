import pytest
from django.urls import reverse
from task_manager.labels.models import Label
from django.core.exceptions import ObjectDoesNotExist
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
        call_command("loaddata", get_fixture("labels.json"))


@pytest.fixture()
def client(client, test_data):
    exist_user = test_data["users"]["existing"]
    client.login(
        username=exist_user["username"],
        password=exist_user["password"],
    )
    yield client


@pytest.mark.django_db
def test_labels_page(client):
    url = reverse("labels:index")
    response = client.get(url)

    assert len(response.context["label_list"]) == 3
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_label(client, test_data):
    new_label = test_data["labels"]["new"]
    url = reverse("labels:create")
    client.post(url, new_label)

    created_label = Label.objects.get(name=new_label["name"])
    assert created_label.name == new_label["name"]


@pytest.mark.django_db
def test_update_label(client, test_data):
    label = test_data["labels"]["existing"]
    new_label = test_data["labels"]["new"]

    existed_label = Label.objects.get(name=label["name"])

    url = reverse("labels:update", args=[existed_label.pk])
    client.post(url, new_label)

    updated_label = Label.objects.get(name=new_label["name"])
    assert updated_label.name == new_label["name"]


@pytest.mark.django_db
def test_delete_label(client, test_data):
    label = test_data["labels"]["existing"]
    existed_label = Label.objects.get(name=label["name"])

    url = reverse("labels:delete", args=[existed_label.pk])
    client.post(url)

    with pytest.raises(ObjectDoesNotExist):
        assert Label.objects.get(name=label["name"])

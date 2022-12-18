import pytest
from django.urls import reverse
from task_manager.tasks.models import Task
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
        call_command("loaddata", get_fixture("statuses.json"))
        call_command("loaddata", get_fixture("labels.json"))
        call_command("loaddata", get_fixture("tasks.json"))
        call_command("loaddata", get_fixture("task_labels.json"))


@pytest.fixture()
def client(client, test_data):
    exist_user = test_data["users"]["existing"]
    client.login(
        username=exist_user["username"],
        password=exist_user["password"],
    )
    yield client


@pytest.mark.django_db
def test_tasks_page(client):
    url = reverse("tasks:index")
    response = client.get(url)

    assert len(response.context["task_list"]) == 3
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_task(client, test_data):
    new_task = test_data["tasks"]["new"]
    url = reverse("tasks:create")
    client.post(url, new_task)

    created_task = Task.objects.get(name=new_task["name"])
    assert created_task.name == new_task["name"]


@pytest.mark.django_db
def test_update_task(client, test_data):
    task = test_data["tasks"]["existing"]
    new_task = test_data["tasks"]["new"]

    existed_task = Task.objects.get(name=task["name"])

    url = reverse("tasks:update", args=[existed_task.pk])
    client.post(url, new_task)

    updated_task = Task.objects.get(name=new_task["name"])
    assert updated_task.name == new_task["name"]


@pytest.mark.django_db
def test_delete_task(client, test_data):
    task = test_data["tasks"]["existing"]
    print("TASKS = ", Task.objects.all())
    existed_task = Task.objects.get(name=task["name"])

    url = reverse("tasks:delete", args=[existed_task.pk])
    client.post(url)

    with pytest.raises(ObjectDoesNotExist):
        assert Task.objects.get(name=task["name"])

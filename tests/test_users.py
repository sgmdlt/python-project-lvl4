import json

import pytest
from conftest import get_fixture
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from task_manager.users.models import User


@pytest.fixture
def test_data():
    return json.loads(open(get_fixture("test_data.json")).read())


def test_home_page(client):
    url = reverse("index")
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_users_page(client):
    url = reverse("users:index")
    response = client.get(url)

    assert len(response.context["user_list"]) == 3
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_user(client, test_data):
    new_user = test_data["users"]["new"]
    url = reverse("users:create")
    client.post(url, new_user)

    created_user = get_user_model().objects.get(username=new_user["username"])
    assert created_user.__str__() == new_user["full_name"]
    assert created_user.first_name == new_user["first_name"]
    assert created_user.last_name == new_user["last_name"]
    assert created_user.username == new_user["username"]


@pytest.mark.django_db
def test_update_user(client, test_data):

    exist_user = test_data["users"]["existing"]
    new_user = test_data["users"]["new"]
    client.login(
        username=exist_user["username"],
        password=exist_user["password"],
    )

    exist_user = get_user_model().objects.get(username=exist_user["username"])
    response = client.post(
        reverse("users:update", args=[exist_user.pk]),
        new_user,
    )

    assert response.status_code == 302
    updated_user = get_user_model().objects.get(username=new_user["username"])
    assert updated_user.__str__() == new_user["full_name"]
    assert updated_user.first_name == new_user["first_name"]
    assert updated_user.last_name == new_user["last_name"]
    assert updated_user.username == new_user["username"]


@pytest.mark.django_db
def test_delete_user(client, test_data):

    exist_user = test_data["users"]["existing"]
    client.login(
        username=exist_user["username"],
        password=exist_user["password"],
    )
    user = get_user_model().objects.get(username=exist_user["username"])
    url = reverse("users:delete", args=[user.pk])
    client.post(url)
    with pytest.raises(ObjectDoesNotExist):
        get_user_model().objects.get(username=exist_user["username"])

import pytest
from django.urls import reverse
from users.models import User


def test_home_page(client):
   url = reverse('home')
   response = client.get(url)
   
   assert response.status_code == 200

@pytest.mark.django_db
def test_no_users_page(client):
   url = reverse('users:users_home')
   response = client.get(url)
   
   assert list(response.context['users_list']) == []
   assert response.status_code == 200


@pytest.mark.django_db
def test_users_page(client):
   user = User.objects.create(
      first_name='Jack',
      last_name='Alltrades',
      username='jack4alltrades',
      )
   url = reverse('users:users_home')
   response = client.get(url)
   
   assert list(response.context['users_list']) == [user]
   assert response.status_code == 200

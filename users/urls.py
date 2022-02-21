from django.urls import path
from users import views

app_name = 'users'
urlpatterns = [
    path('', views.UsersView.as_view(), name='users_home'),
]

from django.urls import path
from users import views

app_name = "users"
urlpatterns = [
    path("", views.UsersView.as_view(), name="index"),
    path("create/", views.RegistrationView.as_view(), name="create"),
]

from django.urls import path
from task_manager.users import views

app_name = "users"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("create/", views.UserCreateView.as_view(), name="create"),
    path("<int:pk>/update/", views.UserUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.UserDeleteView.as_view(), name="delete"),
]

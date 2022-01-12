from django.urls import path
from task_manager import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
]

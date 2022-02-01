from django.contrib import admin
from django.urls import include, path
from task_manager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('users/', include('users.urls')),
]

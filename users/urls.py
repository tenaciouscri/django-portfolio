from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),
]

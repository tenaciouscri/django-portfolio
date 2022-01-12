from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("oauth/", include("social_django.urls")),
    path("register/", views.register, name="register"),
]
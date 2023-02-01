from django.urls import path
from .views import HomeView, AboutView
from projects.views import DashboardView


urlpatterns = [
    path("", DashboardView, name="dashboard"),
    path("about/", AboutView.as_view(), name="about"),
]
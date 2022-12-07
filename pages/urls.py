from django.urls import path
from .views import HomeView, AboutView
from projects.views import ProjectHomeView


urlpatterns = [
    path("", ProjectHomeView, name="project-home"),
    path("about/", AboutView.as_view(), name="about"),
]
from django.urls import path
from .views import ProjectCreateView, ProjectList


urlpatterns = [
    path("create", ProjectCreateView.as_view(), name="project-create"),
    path("all", ProjectList.as_view(), name="project-all"),
]
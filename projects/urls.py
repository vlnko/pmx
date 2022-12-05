from django.urls import path
from .views import ProjectCreateView, ProjectListView, ProjectUpdateView


urlpatterns = [
    path("create", ProjectCreateView.as_view(), name="project-create"),
    path("all", ProjectListView.as_view(), name="project-all"),
    path('update/<int:pk>/', ProjectUpdateView.as_view(),name='project-update'),
]
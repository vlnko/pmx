from django.urls import path
from .views import ProjectCreateView, ProjectListView, ProjectUpdateView, ProjectDetailView


urlpatterns = [
    path("p/create", ProjectCreateView.as_view(), name="project-create"),
    path("", ProjectListView.as_view(), name="project-all"),
    path('p/update/<int:pk>/', ProjectUpdateView.as_view(), name='project-update'),
    path('p/detail/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
]
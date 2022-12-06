from django.urls import path
from .views import ProjectCreateView, ProjectListView, ProjectUpdateView, ProjectDetailView, ProjectDeleteView, TaskCreateView, TaskDetailView, TaskUpdateView, TaskDeleteView


urlpatterns = [
    path("", ProjectListView.as_view(), name="project-all"),
    path("p/create", ProjectCreateView.as_view(), name="project-create"),
    path('p/detail/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('p/update/<int:pk>/', ProjectUpdateView.as_view(), name='project-update'),
    path('p/delete/<int:pk>/', ProjectDeleteView.as_view(), name='project-delete'),
    path("t/create", TaskCreateView.as_view(), name="task-create"),
    path('t/detail/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('t/update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('t/delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
]
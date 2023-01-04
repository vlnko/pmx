from django.urls import path
from .views import *


urlpatterns = [
    # Project urls
    path("p/all/", ProjectListView.as_view(), name="project-all"),
    path("p/create", ProjectCreateView.as_view(), name="project-create"),
    path('p/detail/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('p/update/<int:pk>/', ProjectUpdateView.as_view(), name='project-update'),
    path('p/delete/<int:pk>/', ProjectDeleteView.as_view(), name='project-delete'),
    # Task urls
    path('t/my/', MyTasksView, name='task-my'),
    path('t/get/', getTasks, name='get-tasks'),
    path("t/create/<int:pr_id>", TaskCreateView.as_view(), name="task-create"),
    path('t/detail/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('t/update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('t/delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
    # Task status urls
    path('t/makeinbox/<int:pk>/', TaskMakeInboxView, name='task-make-inbox'),
    path('t/makeworking/<int:pk>/', TaskMakeWorkingView, name='task-make-working'),
    path('t/makechecking/<int:pk>/', TaskMakeCheckingView, name='task-make-checking'),
    path('t/makereworking/<int:pk>/', TaskMakeReworkingView, name='task-make-reworking'),
    path('t/makedone/<int:pk>/', TaskMakeDoneView, name='task-make-done'),
    # Utility urls
    path('getmyprogress/', getMyProgress, name='getmyprogress'), # this is for progress widget
]

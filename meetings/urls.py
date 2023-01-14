from django.urls import path
from .views import *


urlpatterns = [
    path("", MeetingListView.as_view(), name="meetings-all"),
]

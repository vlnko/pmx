from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(r'users', views.CustomUserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("pages.urls")),
    path('meetings', include("meetings.urls")),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("projects/", include("projects.urls"))
]
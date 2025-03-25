from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import TechnologiesViewSet, ProjectViewSet

router = DefaultRouter()
router.register(r"technology", TechnologiesViewSet, basename="technology")
router.register(r"project", ProjectViewSet, basename="project")

urlpatterns = [path("", include(router.urls))]

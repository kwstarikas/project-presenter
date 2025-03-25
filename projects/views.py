from django.shortcuts import render

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from .models import Technology, Project
from .serializers import (
    ProjectSerializer,
    TechnologiesSerializer,
    CompleteProjectSerializer,
)


@extend_schema(tags=["Technologies"])
@extend_schema_view(
    list=extend_schema(
        summary="List all technologies",
        description="This endpoint is used to list all technologies in the database",
    ),
    create=extend_schema(
        summary="Create technology",
        description="This endpoint is used to create a technology with its values",
    ),
    partial_update=extend_schema(
        summary="Upadate a technology",
        description="This endpoint is used to update a technology values",
    ),
    destroy=extend_schema(
        summary="Delete a technology",
        description="This endpoint is used to delete a technology ",
    ),
)
class TechnologiesViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    http_method_names = http_method_names = ["post", "get", "patch", "delete"]
    serializer_class = TechnologiesSerializer
    queryset = Technology.objects.all()


@extend_schema(tags=["Projects"])
@extend_schema_view(
    list=extend_schema(
        summary="List all projects",
        description="This endpoint is used to list all projects in the database",
    ),
    create=extend_schema(
        summary="Create Project",
        description="This endpoint is used to create a project with its values",
    ),
    retrieve=extend_schema(
        summary="Retrieve a project",
        description="This endpoint is used to retrieve a specific project instance based on the path id ",
    ),
    partial_update=extend_schema(
        summary="Upadate a project",
        description="This endpoint is used to update a projects values",
    ),
    complete_project=extend_schema(
        summary="Set a project's end date marking it complete",
        description="This endpoint is used to set the end_time field of a project marking it a complete project",
    ),
)
class ProjectViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
):
    http_method_names = ["post", "get", "patch"]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def get_serializer_class(self):
        if self.action in ["complete_project"]:
            return CompleteProjectSerializer
        return ProjectSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["patch"], name="complete", url_path="complete")
    def complete_project(self, request, *args, **kwargs):
        project = self.get_object()
        serializer = self.get_serializer(data=request.data, instance=project)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

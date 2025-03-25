import datetime
from django.utils.timezone import now
from rest_framework import serializers

from .models import Project, Technology


class TechnologiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ["name"]


class ProjectSerializer(serializers.ModelSerializer):
    technologies = TechnologiesSerializer(many=True)
    # technologies = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Project
        fields = ["id", "name", "description", "technologies"]

        extra_kwargs = {
            "id": {"read_only": True},
        }

    def create(self, validated_data):
        technologies = validated_data.pop("technologies")

        tech = [
            Technology.objects.get_or_create(name=t["name"])[0] for t in technologies
        ]
        pr = Project.objects.create(**validated_data)
        pr.technologies.set(tech)
        validated_data["technologies"] = [{"name": t.name} for t in tech]
        return validated_data


class CompleteProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = []

    def validate(self, attrs):
        print("\n\n\n In validate")

        return attrs

    def update(self, instance, validated_data):
        print("YEAH")
        instance.end_date = now()
        instance.save()
        return validated_data

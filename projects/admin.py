from django.contrib import admin

from .models import Technology, Project


class TechnologeisAdmin(admin.ModelAdmin):
    model = Technology
    list_display = ["id", "name"]
    fields = ["name"]


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ["id", "name", "start_date", "end_date"]
    fields = [
        "name",
        "description",
        "technologies",
    ]


admin.site.register(Technology, TechnologeisAdmin)
admin.site.register(Project, ProjectAdmin)

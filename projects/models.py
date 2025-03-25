from django.db import models


class Technology(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"Technology : {self.name}"


class Project(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    technologies = models.ManyToManyField(Technology)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Project : {self.name}"

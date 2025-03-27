from rest_framework.test import APITestCase

from .models import Project, Technology


class TestProjectCreation(APITestCase):

    def setUp(self):
        self.t1 = Technology.objects.create(name="Python")
        self.t2 = Technology.objects.create(name="Java")

        self.p1 = Project.objects.create(
            name="p1", description="This is a simple description"
        )
        self.p2 = Project.objects.create(
            name="p2", description="This is a simple description"
        )
        self.p1.technologies.set([self.t1, self.t2])
        self.p2.technologies.set([self.t1])

        self.assertEqual(str(self.p2), "Project : p2")
        self.assertEqual(str(self.t2), "Technology : Java")

    def test_get_project(self):
        response = self.client.get(f"/project/{self.t1.id}/")
        self.assertEqual(response.status_code, 200)

    def test_project(self):
        data = {
            "name": "string",
            "description": "string",
            "technologies": [{"name": "string"}],
        }
        response = self.client.post("/project/", data=data, format="json")
        self.assertEqual(response.status_code, 201)

    def test_make_project_complete(self):
        response = self.client.patch(f"/project/{self.p1.id}/complete/")
        self.assertEqual(response.status_code, 200)

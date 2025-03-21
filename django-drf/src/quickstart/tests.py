from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AuthTests(APITestCase):
    def setUp(self):
        self._user_model = get_user_model()
        self._user = self._user_model.objects.create(
            username="test_user",
        )
        self.client.force_authenticate(user=self._user)

    def _test_create(self, view_name, **data):
        response = self.client.post(reverse(view_name), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return response.data

    def test_create_user(self):
        payload = dict(
            username="test_user_two",
            email="test_user@mail.ru",
            password="test_password",
        )
        user = self._test_create("user-list", **payload)
        tuple(
            map(
                lambda k: self.assertEqual(user[k], payload[k]),
                (
                    "username",
                    "email",
                ),
            ),
        )

    def test_create_group(self):
        group = self._test_create(
            "group-list",
            name="test_group",
        )
        self.assertEqual(group["name"], "test_group")

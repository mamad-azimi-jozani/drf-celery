from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.test import APIClient
import pytest


@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_anonymous_return_401(self):
        client = APIClient()
        payload = {
            'title': "a"
        }
        response = client.post('/store/collections/', {"title": "test"})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_return_403(self):
        client = APIClient()
        client.force_authenticate(user={})
        payload = {
            'title': "a"
        }
        response = client.post('/store/collections/', {"title": "test"})
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_valid_return_200(self):
        client = APIClient()
        client.force_authenticate(User(is_staff=True))
        payload = {
            'title': "a"
        }
        response = client.post('/store/collections/', {"title": "test"})
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0


import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from profiles.api.serializers import ProfileSerializer
from profiles.models import Profile


class RegistrationTestCase(APITestCase):

	def test_registration(self):
		data = {
			"username": "testcase",
			"email": "test@localhost.app",
			"password1": "some_strong_pw",
			"password2": "some_strong_pw",
		}

		response = self.client.post("/api/rest-auth/registration/", data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
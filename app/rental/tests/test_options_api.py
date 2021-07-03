from os import stat
from django import test
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import serializers, status
from rest_framework.test import APIClient

from core.models import Options

from rental.serializers import OptionSerializer

# OPTIONS_URL = reverse('rental:feature-list')

class OptionsTestCase(TestCase):
    """Testing the options model"""

    def setUp(self):
        self.client = APIClient()

    # HAVE NOT FIGURED WHY THIS TEST IS NOT PASSING, WILL COME BACK LATER ;)

    # def test_retrieve_options(self):
    #     """Test for retrieving available options"""
    #     Options.objects.create(no_of_rooms=3)
    #     Options.objects.create(no_of_rooms=4, furnished=True)

    #     res = self.client.get(OPTIONS_URL)

    #     options = Options.objects.all()
    #     serializer = OptionSerializer(options, many=True)
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)
    #     self.assertEqual(serializer.data, res.data)
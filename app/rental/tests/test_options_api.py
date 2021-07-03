from django import test
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Options

# from rental.serializers import OptionSerializer

class OptionsTestCase(TestCase):
    """Testing the options model"""

    def setUp(self):
        self.client = APIClient()
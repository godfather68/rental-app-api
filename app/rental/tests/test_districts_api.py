from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import District

from rental.serializers import DistrictSerializer

DISTRICTS_URL = reverse('rental:district-list')

class PublicDistrictsApiTests(TestCase):
    """Test the publicly available API routes"""
    
    def setUp(self):
        self.client = APIClient()

    def test_retrieve_districts(self):
        """Test that all the district are being retrieved"""
        District.objects.create(name='Lafayette')
        District.objects.create(name='Downtown LA')

        res = self.client.get(DISTRICTS_URL)

        districts = District.objects.all().order_by('-name')
        serializer = DistrictSerializer(districts, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, res.data)
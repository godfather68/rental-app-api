from django import test
from django.db.models.base import Model
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient

from core.models import House, District, Options

from rental.serializers import HouseSerializer, HouseListSerializer, HouseDetailSerializer

HOUSES_URL = reverse('rental:house-list')

def detail_url(house_id):
    """Return house details URL"""
    return reverse('rental:house-detail', args=[house_id])

def sample_district(name='Downtown Lafayette'):
    """Create and return a sample district"""
    return District.objects.create(name=name)

def sample_options(rooms=3):
    """Create and return a sample house options"""
    return Options.objects.create(no_of_rooms=rooms)

def sample_house(user, **params):
    """Create a return a sample house Ad"""
    defaults = {
        'title': '2 bedrooms appartment near metrostation',
        'price': 650.00,
        'description': 'beautiful house downtown lafayette',
        'location': sample_district(),
        'options': sample_options()
    }
    defaults.update(params)

    return House.objects.create(user=user, **defaults)

class PublicHouseTestApi(TestCase):
    """Test the publicly available houses API"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test@nihutie.com',
            'test123'
        )

    def test_access_houses_url(self):
        """Test for retrieving all the available houses"""
        res = self.client.get(HOUSES_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_retrieve_houses(self):
        """Test for retrieving a list of houses"""
        sample_house(user=self.user)
        res = self.client.get(HOUSES_URL)

        houses = House.objects.all().order_by('-id')
        serializer = HouseListSerializer(houses, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_view_house_detail(self):
        """Test viewing a house detail"""
        house = sample_house(user=self.user)

        url = detail_url(house.id)
        res = self.client.get(url)

        serializer = HouseDetailSerializer(house)
        self.assertEqual(res.data, serializer.data)

class PrivateHouseTestApi(TestCase):
    """Privately held API endpoints"""
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test@nihutie.com',
            'test123'
        )
        self.client.force_authenticate(self.user)

    def test_create_house(self):
        """Test for creating an House ad"""
        location = sample_district(name='Alba')
        options = sample_options(rooms=4)
        payload = {
            'title': '2 bedrooms appartment near metrostation',
            'price': 650.00,
            'description': 'beautiful house downtown lafayette',
            'location': location.id,
            'options': options.id,
            'user': self.user
        }

        res = self.client.post(HOUSES_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        house = House.objects.get(id=res.data['id'])
        self.assertEqual(res.data['price'], str(getattr(house, "price")))

    def test_partial_update_house(self):
        """Test updating a house with patch"""
        house = sample_house(user=self.user)
        payload = {
            'title': 'new_location'
        }
        url = detail_url(house.id)
        self.client.patch(url, payload)

        house.refresh_from_db()
        self.assertEqual(house.title, payload['title'])

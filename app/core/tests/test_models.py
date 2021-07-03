from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a user with email is successful"""
        email = "test@nihutie.com"
        password = 'password1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
 
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test for the new user email to be normalized"""
        email = 'test@NIHUTIE.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test creating user with no email raises an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """ Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@nihutie.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_district_str(self):
        """Test the District string representation"""
        district = models.District.objects.create(
            name='St Bruno'
        )

        self.assertEqual(str(district), district.name)

    def test_no_of_rooms_less_than_or_equal_to_five(self):
        """Test that the no of rooms options is <= to 5"""
        option1 = models.Options.objects.create(no_of_rooms = 5)
        option2 = models.Options.objects.create(no_of_rooms = 6)

        self.assertLessEqual(option1.no_of_rooms, 5)
        self.assertNotEqual(option2.no_of_rooms, 5)
        
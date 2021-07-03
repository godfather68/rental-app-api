from django.core import validators
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """ Creates and Save a new User """
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user 

    def create_superuser(self, email, password):
        """Creates and saves a new Super user"""
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """ Custom User model supporting using Email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class District(models.Model):
    """Model for representing the district object"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Options(models.Model):
    """Model for representing options objects"""
    no_of_rooms = models.PositiveSmallIntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
        ]
    )
    furnished = models.BooleanField(default=False)
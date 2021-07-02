from django.urls import path
from django.urls.conf import include
from rest_framework import urlpatterns
from rest_framework import routers

from rest_framework.routers import DefaultRouter

from rental import views

router = DefaultRouter()
router.register('districts', views.DistrictViewSet)

app_name = 'rental'

urlpatterns = [
    path('', include(router.urls))
]
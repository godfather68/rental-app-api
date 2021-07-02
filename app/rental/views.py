from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

from core.models import District

from rental import serializers

class DistrictViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage district viewsets"""
    queryset = District.objects.all()
    serializer_class = serializers.DistrictSerializer

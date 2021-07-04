from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

from core.models import District, Options, House

from rental import serializers

class DistrictViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage district viewsets"""
    queryset = District.objects.all()
    serializer_class = serializers.DistrictSerializer

class OptionViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage Options viewsets"""
    queryset = Options.objects.all()
    serializer_class = serializers.OptionSerializer

class HouseViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage Houses viewsets"""
    serializer_class = serializers.HouseSerializer
    queryset = House.objects.all()
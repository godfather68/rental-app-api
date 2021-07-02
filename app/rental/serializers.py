from rest_framework import serializers

from core.models import District

class DistrictSerializer(serializers.ModelSerializer):
    """Serializer for the District object"""
    
    class Meta:
        model = District
        fields = ('id', 'name')
        read_only_fields = ('id', )
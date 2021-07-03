from rest_framework import serializers

from core.models import District, Options

class DistrictSerializer(serializers.ModelSerializer):
    """Serializer for the District object"""
    
    class Meta:
        model = District
        fields = ('id', 'name')
        read_only_fields = ('id', )

class OptionSerializer(serializers.ModelSerializer):
    """Serializer for the Options object"""

    class Meta:
        model = Options
        fields = ('id', 'no_of_rooms', 'furnished')
        read_only_fields = ('id', )
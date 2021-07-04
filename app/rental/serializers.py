from rest_framework import serializers

from core.models import District, Options, House

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

class HouseSerializer(serializers.ModelSerializer):
    """Serializer for the House ad object"""
    options = serializers.PrimaryKeyRelatedField(
        queryset=Options.objects.all()
    )
    location = serializers.PrimaryKeyRelatedField(
        queryset=District.objects.all()
    )

    class Meta:
        model = House
        fields = ('id', 'title', 'price', 'description','options', 'location', 'furnished')
        read_only_fields = ('id', )
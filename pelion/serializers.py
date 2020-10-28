from rest_framework import serializers
from . import models


class AttributesSerializer(serializers.ModelSerializer):
    """Serializers a user profile object"""

    class Meta:
        model = models.Attribute
        fields = (
            'conf',
            'value',
            'key'
        )



class EventSerializer(serializers.ModelSerializer):
    """Serializers a user profile object"""
    attributes = AttributesSerializer()

    class Meta:
        model = models.Event
        fields = (
            'deviceId',
            'deviceName',
            'personId',
            'personName',
            'attributes'
        )

    def create(self, validated_data):
        attributes_data = validated_data.pop('attributes')
        event = models.Event.objects.create(**validated_data)
        Attribute.objects.create(event=event, **attributes_data)
        return event

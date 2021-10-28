from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serialize a name field to testing an app"""
    name = serializers.CharField(max_length=10)
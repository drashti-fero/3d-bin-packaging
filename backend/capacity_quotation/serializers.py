from rest_framework import serializers
from . import models


class PackagingSpacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PackagingSpaces
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = "__all__"

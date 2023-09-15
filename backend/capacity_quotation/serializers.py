from rest_framework import serializers
from . import models


class PackagingSpacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PackagingSpaces
        fields = "__all__"

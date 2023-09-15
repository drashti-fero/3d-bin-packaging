from rest_framework import serializers
from . import models
from lib import helpers


class PackagingSpacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PackagingSpaces
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = "__all__"


class OptionSerializer(serializers.Serializer):
    FILTER = "filter"
    FORM = "form"

    REQUEST_TYPE_CHOICES = ((FILTER, "Filter"), (FORM, "Form"))

    request_type = serializers.ChoiceField(
        choices=REQUEST_TYPE_CHOICES,
        error_messages={
            "invalid_choice": f"Choices are: {', '.join([request_type[0] for request_type in REQUEST_TYPE_CHOICES])}"
        },
    )

    class Meta:
        fields = ("request_type",)

    def validate(self, attrs):
        request_type = attrs["request_type"]
        data = {}
        if request_type == self.FILTER:
            data = self.get_filter_data()
        elif request_type == self.FORM:
            data = self.get_forms_data()

        return data

    def get_filter_data(self):
        return {}

    def get_forms_data(self):
        return {}


class PackagingSpacesOptionSerializer(OptionSerializer):
    def get_forms_data(self):
        return {
            "packaging_type": helpers.get_option_data(choices_data=models.PackagingSpaces.PACKAGING_TYPE_CHOICES),
        }

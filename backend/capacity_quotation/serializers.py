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


class BinsDataForPayload(serializers.ModelSerializer):
    w = serializers.CharField(source="width")
    h = serializers.CharField(source="height")
    d = serializers.CharField(source="length")
    id = serializers.CharField(source="packaging_space_id")
    type = serializers.CharField(source="packaging_type")

    class Meta:
        model = models.PackagingSpaces
        fields = ("w", "h", "d", "id", "type")


class ItemsDataForPayload(serializers.ModelSerializer):
    w = serializers.CharField(source="width")
    h = serializers.CharField(source="height")
    d = serializers.CharField(source="length")
    id = serializers.CharField(source="sku")
    wg = serializers.CharField(source="weight")

    class Meta:
        model = models.Item
        fields = ("w", "h", "d", "id", "wg")


class ItemCapacityQuotationSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(queryset=models.Item.objects.all())
    quantity = serializers.IntegerField(min_value=1)

    class Meta:
        model = models.Item
        fields = ("id", "quantity")

    def validate(self, attrs):
        item_object = attrs.pop("id")
        attrs.update(**ItemsDataForPayload(instance=item_object).data)
        attrs.update({"q": attrs.pop("quantity")})
        return attrs


class CapacityQuotationSerializer(serializers.ModelSerializer):
    bins = serializers.PrimaryKeyRelatedField(many=True, queryset=models.PackagingSpaces.objects.all())
    items = ItemCapacityQuotationSerializer(many=True)

    class Meta:
        model = models.CapacityQuotation
        fields = ("bins", "items", "ref_no")

    def validate_bins(self, value):
        bins_data = []
        for packaging_spaces_instance in value:
            bins_data.append(
                BinsDataForPayload(instance=packaging_spaces_instance, context=self.context).data
            )

        return bins_data

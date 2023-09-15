from django.db import models
from django.core import validators
from model_utils.models import TimeStampedModel


# Create your models here.
class PackagingSpaces(TimeStampedModel):
    PACKAGING_TYPE_CHOICES = (
        ("box", "Box"),
        ("create", "Create"),
        ("container", "Container"),
        ("pallet", "Pallet"),
        ("vehicle", "Vehicle"),
    )
    packaging_space_id = models.CharField(unique=True, max_length=255)
    length = models.DecimalField(
        decimal_places=2, max_digits=10, validators=[validators.MinValueValidator(0)]
    )
    width = models.DecimalField(
        decimal_places=2, max_digits=10, validators=[validators.MinValueValidator(0)]
    )
    height = models.DecimalField(
        decimal_places=2, max_digits=10, validators=[validators.MinValueValidator(0)]
    )
    weight = models.DecimalField(
        decimal_places=2, max_digits=10, validators=[validators.MinValueValidator(0)]
    )
    max_weight_capacity = models.DecimalField(
        decimal_places=2, max_digits=10, validators=[validators.MinValueValidator(0)]
    )
    packaging_type = models.CharField(choices=PACKAGING_TYPE_CHOICES)


class Item(TimeStampedModel):
    sku = models.CharField(unique=True, max_length=255)
    length = models.DecimalField(
        decimal_places=2, max_digits=10, validators=[validators.MinValueValidator(0)]
    )
    width = models.DecimalField(
        decimal_places=2, max_digits=10, validators=[validators.MinValueValidator(0)]
    )
    height = models.DecimalField(
        decimal_places=2, max_digits=10, validators=[validators.MinValueValidator(0)]
    )
    weight = models.DecimalField(
        decimal_places=2, max_digits=10, validators=[validators.MinValueValidator(0)]
    )


class CapacityQuotation(TimeStampedModel):
    ref_no = models.CharField(max_length=255)
    payload = models.JSONField()
    response = models.JSONField()

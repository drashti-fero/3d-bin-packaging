from django.contrib import admin
from django.db.models import JSONField
from django_json_widget.widgets import JSONEditorWidget
from .models import PackagingSpaces, Item, CapacityQuotation


class PackagingSpacesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'packaging_space_id',
        'length',
        'width',
        'height',
        'weight',
        'max_weight_capacity',
        'packaging_type',
    )
    list_filter = (
        'created',
        'modified',
        'id',
        'packaging_space_id',
        'length',
        'width',
        'height',
        'weight',
        'max_weight_capacity',
        'packaging_type',
    )


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'sku',
        'length',
        'width',
        'height',
        'weight',
    )
    list_filter = (
        'created',
        'modified',
        'id',
        'sku',
        'length',
        'width',
        'height',
        'weight',
    )


class CapacityQuotationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'ref_no',
        'payload',
        'response',
    )
    list_filter = (
        'created',
        'modified',
        'id',
        'ref_no',
        'payload',
        'response',
    )
    formfield_overrides = {JSONField: {"widget": JSONEditorWidget}}


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(PackagingSpaces, PackagingSpacesAdmin)
_register(Item, ItemAdmin)
_register(CapacityQuotation, CapacityQuotationAdmin)

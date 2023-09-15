from . import models, serializers
from lib.views import BaseViewSet
from lib import constants
from rest_framework.response import Response
from rest_framework import status
from utils import api_wrapper


# Create your views here.
class PackagingSpacesViewSet(BaseViewSet):
    authentication_classes = []
    permission_classes = []
    model = models.PackagingSpaces
    view_serializers = {
        constants.Action.LIST: serializers.PackagingSpacesSerializer,
        constants.Action.RETRIEVE: serializers.PackagingSpacesSerializer,
        constants.Action.SELECT: serializers.PackagingSpacesSerializer,
        constants.Action.OPTION: serializers.PackagingSpacesOptionSerializer,
    }


class ItemsViewSet(BaseViewSet):
    authentication_classes = []
    permission_classes = []
    model = models.Item
    view_serializers = {
        constants.Action.LIST: serializers.ItemSerializer,
        constants.Action.RETRIEVE: serializers.ItemSerializer,
        constants.Action.SELECT: serializers.ItemSerializer,
    }


class CapacityQuotationViewSet(BaseViewSet):
    authentication_classes = []
    permission_classes = []
    model = models.CapacityQuotation
    view_serializers = {
        constants.Action.LIST: serializers.ItemSerializer,
        constants.Action.RETRIEVE: serializers.CapacityQuotationSerializer,
    }

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        payload = serializer.validated_data
        api = api_wrapper.ThreeDBinPackingAPI(payload=payload)
        response = api.make_request()
        models.CapacityQuotation.objects.create(payload=api.payload, response=response)
        return Response(response, status=status.HTTP_201_CREATED)

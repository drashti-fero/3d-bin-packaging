from . import models, serializers
from lib.views import BaseViewSet
from lib import constants


# Create your views here.
class PackagingSpacesViewSet(BaseViewSet):
    authentication_classes = []
    permission_classes = []
    model = models.PackagingSpaces
    view_serializers = {
        constants.Action.LIST: serializers.PackagingSpacesSerializer,
        constants.Action.RETRIEVE: serializers.PackagingSpacesSerializer,
        constants.Action.SELECT: serializers.PackagingSpacesSerializer,
    }

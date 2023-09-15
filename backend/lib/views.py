import logging

from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from . import constants

logger = logging.getLogger(__name__)


class BaseGenericViewSet(viewsets.GenericViewSet):
    model = None
    filterset_class = None

    class Meta:
        abstract = True


class BaseViewSet(viewsets.ModelViewSet):
    model = None
    filterset_class = None
    view_serializers = {}
    http_method_names = [
        constants.Method.GET,
        constants.Method.HEAD,
        constants.Method.OPTIONS,
        constants.Method.POST,
        constants.Method.PATCH,
        constants.Method.PUT,
    ]

    def get_queryset(self):
        return self.model.objects.all()

    def get_serializer_class(self):
        serializer_dict = self.view_serializers

        if not serializer_dict:
            return self.serializer_class

        request_action = self.action
        if request_action == constants.Action.LIST:
            return serializer_dict[request_action]
        return serializer_dict[constants.Action.RETRIEVE]

    @action(methods=[constants.Method.GET], detail=True)
    def view(self, *args, **kwargs):
        obj = self.get_object()
        serializer = self.view_serializers[self.action](obj, context={"request": self.request})
        return Response(serializer.data)

    @action(
        methods=[constants.Method.GET],
        detail=False,
        permission_classes=[],
    )
    def select(self, *args, **kwargs):

        queryset = self.get_queryset()
        filtered_queryset = self.filter_queryset(queryset=queryset)
        context = self.get_serializer_context()

        paginated_queryset = self.paginate_queryset(filtered_queryset)
        if paginated_queryset is not None:
            serializer = self.view_serializers[self.action](paginated_queryset, many=True, context=context)
            return self.get_paginated_response(serializer.data)

        return Response(self.view_serializers[self.action](filtered_queryset, many=True, context=context).data)

    @action(methods=[constants.Method.GET], detail=False)
    def options(self, request, *args, **kwargs):
        serializer = self.view_serializers[self.action](
            data=request.query_params, context=self.get_serializer_context()
        )
        if serializer.is_valid():
            return Response(serializer.validated_data)
        return Response(serializer.errors)

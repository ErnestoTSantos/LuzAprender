import logging

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_501_NOT_IMPLEMENTED

from pampulha.apps.anamnesis.exceptions import MonitoringSheetException
from pampulha.apps.anamnesis.models import AnamnesisModels, MonitoringSheetModels
from pampulha.apps.anamnesis.serializer import (
    CreateAnamnesisSerializer,
    CreateMonitoringSheetSerializer,
    MonitoringSheetSerializer,
)


class MonitoringSheetModelViewset(viewsets.ModelViewSet):
    queryset = MonitoringSheetModels.objects.order_by("-created_at").all()

    SERIALIZER_ACTION = {
        "create": CreateMonitoringSheetSerializer,
        "list": MonitoringSheetSerializer,
        "retrive": MonitoringSheetSerializer,
        "partial_update": MonitoringSheetSerializer,
        "update": ...,
        "destroy": ...,
    }

    def get_serializer_class(self):
        """
        GET appropriate serializer for the action.
        """

        action = self.action

        return self.SERIALIZER_ACTION[action]

    def _create_monitoring_sheet(self, request, *args, **kwargs):
        logging.info("Creating a new monitoring sheet...")

        logging.info("Starting serializer data...")
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)

        if not serializer.is_valid():
            logging.warning("Something happened in validation... %s", serializer.errors)
            raise MonitoringSheetException(serializer.errors)

        self.perform_create(serializer=serializer)

        return Response(status=HTTP_201_CREATED)

    def create(self, request, *args, **kwargs) -> Response:
        """
        Create new Monitoring sheet.

        Exemple HTTP POST payload:
        {
            name: str,
            birthday: date,
            phone_number: str(51999999999),
            telephone_number str(5199999999),
            cep: str,
            address: str,
            neighborhood: str,
            state: str,
            city: str,
            sex: str,
            recommendation: str,
            entry_date: date,
            specialist_monitoring: str,
            head_teacher: str,
            extra_information: str
        }
        """
        return self._create_monitoring_sheet(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        """
        GET monitoring sheet informations.
        """
        return super().list(self.queryset, request, *args, **kwargs)

    def retrieve(self, request, pk, *args, **kwargs):
        """
        GET data an especific monitoring sheet.
        """
        return super().retrieve(request, pk, *args, **kwargs)

    def partial_update(self, request, pk, *args, **kwargs):
        """
        PUT data an specific monitoring sheet.
        """
        return super().partial_update(request, pk, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Method not implemented
        """

        return Response(HTTP_501_NOT_IMPLEMENTED)

    def update(self, request, *args, **kwargs):
        """
        Method not implemented
        """

        return Response(HTTP_501_NOT_IMPLEMENTED)

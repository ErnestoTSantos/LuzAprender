from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from pampulha.apps.users.serializers import validate_user_token
from pampulha.apps.schedule.serializer import calendarSerializer


class CalendarViewset(viewsets.ModelViewSet):
    serializer_class = calendarSerializer
    http_method_names = ["get", "post", "patch", "delete"]

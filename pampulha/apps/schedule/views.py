from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from pampulha.apps.users.serializers import validate_user_token
from pampulha.apps.schedule.serializer import calendarSerializer


class CalendarViewset(viewsets.ModelViewSet):
    serializer_class = calendarSerializer
    http_method_names = ["get", "post", "patch", "delete"]

    def post(self, request, *args, **kwargs):
        user = validate_user_token(request)
        if not user:
            return Response({"detail": user}, status=status.HTTP_401_UNAUTHORIZED)

        data = request.data
        data.update(
            {
                "psychologist": user
            }
        )
        serializer = calendarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.create(validated_data=serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)

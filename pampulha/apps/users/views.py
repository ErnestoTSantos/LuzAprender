from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from pampulha.apps.users.serializers import JWTAuthentication
from pampulha.apps.users.models import PsychologistModel
from pampulha.apps.users.serializers import PsychologistSerializer


class PsychologistViewset(ModelViewSet):
    serializer_class = PsychologistSerializer
    queryset = PsychologistModel.objects.all()
    http_method_names = ["post", ]

    @action(methods=["POST"], detail=False, url_path="login")
    def login(self, request, *args, **kwargs):
        validated_data = JWTAuthentication.validate_user(self, request.data)
        return Response(data=validated_data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = PsychologistSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.create(validated_data=serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)

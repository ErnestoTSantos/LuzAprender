from django.contrib.auth.hashers import check_password
from rest_framework import permissions, status, views
from rest_framework.response import Response

from pampulha.apps.management.api.serializers import ObtainTokenSerializer
from pampulha.apps.management.authentication import JWTAuthentication
from pampulha.apps.users.models import PsychologistModel


class ObtainTokenView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ObtainTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        username_or_phone_number = serializer.validated_data.get("username")
        password = serializer.validated_data.get("password")

        user = PsychologistModel.objects.filter(
            username=username_or_phone_number
        ).first()
        if user is None:
            raise "username or password is invalid."

        if user is None or not check_password(password, user.password):
            return Response(
                {"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST
            )

        # Generate the JWT token
        jwt_token = JWTAuthentication.create_jwt(user)

        return Response({"token": jwt_token})

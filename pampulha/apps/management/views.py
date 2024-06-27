from django.conf import settings
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.views import TokenViewBase

from pampulha.apps.management.api.serializers import (
    AuthenticationSerializer,
    AuthenticationVerifySerializer,
)
from pampulha.apps.management.authentication import authenticate_user


class AuthenticationView(TokenViewBase):
    serializer_class = AuthenticationSerializer


class AuthenticationVerifyView(TokenViewBase):
    serializer_class = AuthenticationVerifySerializer


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@authentication_classes([IsAuthenticated])
def loggin(request: Request):
    """
    Route to user loggin
    """

    username = request.data.get("username")
    password = request.data.get("password")

    if not username:
        return Response(
            {
                "error": {
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "Missing username!",
                }
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    if not password:
        return Response(
            {
                "error": {
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": "Missing password!",
                }
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    user_informations = {"username": username, "password": password}

    if authenticate_user(username=username, password=password):
        token = AuthenticationSerializer.get_token(user_informations)
        return Response(
            {
                "token": str(token),
                "redirect_url": f"{settings.REDIRECT_ROUTE_LOGGIN}{str(token)}",
            },
            status=status.HTTP_200_OK,
        )

    raise AuthenticationFailed(
        detail="Username or password invalid", code=status.HTTP_401_UNAUTHORIZED
    )

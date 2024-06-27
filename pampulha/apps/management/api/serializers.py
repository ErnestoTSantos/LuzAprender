from typing import Dict

from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import (
    TokenObtainSerializer,
    TokenVerifySerializer,
)
from rest_framework_simplejwt.tokens import AccessToken

from pampulha.apps.management.authentication import authenticate_user


class AuthenticationSerializer(TokenObtainSerializer):
    @classmethod
    def get_token(cls, information: Dict) -> AccessToken:
        token = AccessToken()
        token["user_information"] = information
        return token

    def validate(self, attrs: Dict) -> Dict:
        username, password = attrs["username"], attrs["password"]

        if not authenticate_user(username=username, password=password):
            raise AuthenticationFailed(
                detail="Username or password invalid", code=HTTP_401_UNAUTHORIZED
            )

        token = self.get_token(attrs)

        return {"token": str(token)}


class AuthenticationVerifySerializer(TokenVerifySerializer):
    def validate(self, attrs: Dict):
        token = AccessToken(token=attrs["token"])
        return token.payload

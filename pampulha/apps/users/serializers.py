import re
import jwt
import json

from django.db import transaction
from django.conf import settings
from django.contrib.auth.hashers import check_password

from rest_framework import authentication
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.exceptions import ParseError

from pampulha.apps.users.models import PsychologistModel

class JWTAuthentication(authentication.BaseAuthentication):
    def validate_user(self, data):
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            raise AuthenticationFailed(detail="Email or password is invalid.")

        try:
            psycologist = PsychologistModel.objects.get(username=username)
        except PsychologistModel.DoesNotExist:
            raise AuthenticationFailed(detail="Email or password is invalid.")

        if not check_password(password, encoded=psycologist.password):
            raise AuthenticationFailed(detail="Email or password is invalid.")

        return JWTAuthentication.create_jwt(psycologist)

    def authenticate(self, request):
        jwt_token = request.META.get("HTTP_AUTHORIZATION")

        if jwt_token is None or not jwt_token.startswith("Bearer "):
            raise AuthenticationFailed("Bearer token not found")

        jwt_token = JWTAuthentication.get_the_token_from_header(jwt_token)

        try:
            payload = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=["HS256"])
        except jwt.exceptions.InvalidSignatureError:
            raise AuthenticationFailed("Invalid signature")
        except jwt.exceptions.ExpiredSignatureError:
            raise AuthenticationFailed("Token has expired")
        except:
            raise ParseError()

        user_id = payload.get("id")
        if user_id is None:
            raise AuthenticationFailed("User identifier not found in JWT")

        return user_id

    @classmethod
    def create_jwt(cls, user):
        token = {
            "id": str(user.id),
            "name": user.name,
            "username": user.username,
            "age": user.age,
            "gender": user.get_gender_display()
        }

        return token

    @classmethod
    def get_the_token_from_header(cls, token):
        token = token.replace("Bearer", "").replace(" ", "")
        return token


def validate_user_token(request):
    auth = JWTAuthentication
    user_id = auth.authenticate(auth, request=request)

    try:
        return PsychologistModel.objects.get(id=user_id)
    except PsychologistModel.DoesNotExist:
        raise AuthenticationFailed("User not found")


class PsychologistSerializer(serializers.ModelSerializer):
    def validate_username(self, username):
        if len(username) < 5:
            raise "username must be at least 5 characters."

        return username

    def validate_password(self, password):
        special_chars = re.search("[@_!#$%^&*()<>?/\|}{~:]", password)

        if len(password) < 8:
            raise serializers.ValidationError("password must be at least 8 characters.")

        if special_chars is None:
            raise serializers.ValidationError("password need special characters.")

        return password

    class Meta:
        model = PsychologistModel
        fields = "__all__"

    @transaction.atomic
    def create(self, validated_data):
        return PsychologistModel.objects.create(**validated_data)

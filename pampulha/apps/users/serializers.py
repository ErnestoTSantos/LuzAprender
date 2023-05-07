import re

from rest_framework.serializers import ModelSerializer

from pampulha.apps.users.models import PsychologistModel


class PsychologistSerializer(ModelSerializer):
    def validate_username(self, username):
        if len(username) < 5:
            raise "username must be at least 5 characters."

        return username

    def validate_password(self, password):
        special_chars = re.search("[@_!#$%^&*()<>?/\|}{~:]")

        if len(password) < 8:
            raise "password must be at least 8 characters."

        if special_chars(password) is None:
            raise "password need special characters."

        return password

    def validate_user_data(self, data):
        first_name = data["first_name"]
        last_name = data["last_name"]
        birthday = data["birthday"]
        data["profission"] = "Psychologist"

        if not first_name:
            raise "User need a first_name."

        if not last_name:
            raise "User need a last_name."

        if not birthday:
            raise "User need a birtday date."

    def validate(self, attrs):
        password = attrs["password"]
        password_confirmation = attrs["password_confirmation"]

        if password != password_confirmation:
            raise "passwords do not match."

        return attrs

    class Meta:
        model = PsychologistModel
        fields = "__all__"

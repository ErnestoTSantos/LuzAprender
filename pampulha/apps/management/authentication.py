from django.contrib.auth.hashers import check_password

from pampulha.apps.users.models import PsychologistModel


def authenticate_user(username: str, password: str):
    user = PsychologistModel.objects.filter(username=username).first()

    if not user:
        return False

    if not check_password(password=password, encoded=user.password):
        return False

    return True

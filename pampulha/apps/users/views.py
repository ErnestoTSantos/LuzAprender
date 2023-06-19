from rest_framework.decorators import action, permission_classes
from rest_framework.viewsets import ModelViewSet

from pampulha.apps.users.models import PsychologistModel
from pampulha.apps.users.serializers import PsychologistSerializer


class PsychologistViewset(ModelViewSet):
    @action(methods=["POST"], detail=False, url_path="login")
    def login(self, request, *args, **kwargs):
        ...

    def create(self, request, *args, **kwargs):
        ...

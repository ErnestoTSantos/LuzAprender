import logging

from rest_framework import viewsets
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_501_NOT_IMPLEMENTED

from pampulha.apps.anamnesis.exceptions import MonitoringSheetException
from pampulha.apps.anamnesis.models import AnamnesisModels, MonitoringSheetModels
from pampulha.apps.anamnesis.serializer import (
    AnamnesisSerializer,
    CreateAnamnesisSerializer,
    CreateMonitoringSheetSerializer,
    MonitoringSheetSerializer,
)


class PsychologistPermission(BasePermission):
    def has_permission(self, request, view):
        return True


class AnamnesisModelViewset(viewsets.ModelViewSet):
    queryset = AnamnesisModels.objects.all().order_by("-created_at")
    http_method_names = ["get", "post", "patch", "options"]

    SERIALIZER_ACTION = {
        "create": CreateAnamnesisSerializer,
        "list": AnamnesisSerializer,
        "retrieve": AnamnesisSerializer,
        "partial_update": AnamnesisSerializer,
        "update": ...,
        "destroy": ...,
    }

    def get_serializer_class(self):

        action = self.action

        return self.SERIALIZER_ACTION[action]

    def _create_anamnesis(self, request, *args, **kwargs):
        logging.info("Creating a new anamnesis...")
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)

        if not serializer.is_valid():
            logging.warning("Something happened in validation... %s", serializer.errors)
            raise MonitoringSheetException(serializer.errors)

        self.perform_create(serializer=serializer)

        return Response(status=HTTP_201_CREATED)

    def create(self, request, *args, **kwargs) -> Response:
        """
        Create new anamnesis.

        Exemple HTTP POST payload:
        {
            "name": "Marcio Freitas",
            "birthday": "17/10/2005",
            "phone_number": "51999999999",
            "address": "Quinze de novembro",
            "age": 10,
            "father": "Luciano Freitas",
            "father_age": 30,
            "father_schooling": "Ensino superior completo",
            "father_profission": "Personal trainer",
            "mother": "Juliana Passos",
            "mother_age": 26,
            "mother_schooling": "Ensino superior incompleto",
            "mother_profession": "Auxiliar de contabilidade",
            "birth_position": "Filho único",
            "family_complaint": "O filho é extremamente quieto, não consegue realizar ações com outras crianças",
            "pregnancy_history": "Não foi planejado",
            "prenatal_care": "Foi realizada diversas ações com médicos, acompanhamento certo, com tudo que a criança necessita.",
            "where_was": "No hospital getúlio vargas",
            "type_of_delivery": "Normal",
            "on_the_expected_date": false,
            "complications": "Sem complicações",
            "color": "Branco",
            "weight": 3.54,
            "measure": 0.40,
            "needed_hospitalize": "Não",
            "how_much_time": "3 Horas de parto",
            "reason": "Dificuldade pelo posicionamento do bebê",
            "medication": "Sem medicações",
            "performed_surgery": "Não",
            "First_contact_with_chest": "2 Horas após seu nascimento",
            "sucking_swallowing_difficulties": false,
            "when_stop_breastfeeding": "8 meses",
            "used_bottle": true,
            "used_acifier": true,
            "start_solid_food": "7 meses",
            "reactions": "Adorou a alimentação sólida",
            "had_eating_difficulties": "Zero dificuldades",
            "current_power": "Alimentos sólidos e liquidos, sem problemas.",
            "shared_bed": false,
            "sleep": "Calmo, porém, precisava estar alimentado",
            "wake_up": "Com fome",
            "sleeping_rituals": "Sem rituais",
            "currently_sleep": "Sozinho e sem grandes dificuldades",
            "first_speech": "9 meses",
            "accompanied": "Pai",
            "currently_speak": "De maneira clara",
            "language_disorders": "Utilizando desenhos",
            "other_media": "Muitas mensagens",
            "sat": "4 meses",
            "crawled": "4 meses",
            "start_walk": "9 meses",
            "fence_walker": "Utilizou cercado",
            "tendency_fall": "Não",
            "accidents": "Não sofreu acidentes",
            "swings_other_movements": "Normais",
            "father_presence_absence": "Pai extremamente presente, cumprindo com seu papel",
            "mother_conduct": "Próxima, porém, muito protetora",
            "removal_diapers": "Difícil, não foi fácil aprender a utilizar o banheiro",
            "nocturnal_enuresis": "Não",
            "encomprese": "Não",
            "who_play_with": "Amigos da creche",
            "how_play": "Jogos e brincadeiras, além, dos video games",
            "favorite_toys_games": "Video game e jenga",
            "attitudes_towards_toys": "Normal",
            "start_drawing": "2 anos",
            "conduct": "Normal",
            "curious": true,
            "observer": true,
            "happy": false,
            "good_memory": true,
            "aggressive": true,
            "stubborn": true,
            "make_friends": false,
            "affective": false,
            "withdrawn": true,
            "dependent": true,
            "changeable_mood": true,
            "reaction_upset": "De maneira agressiva, tenta ter o controle da situação",
            "relationship_father": "De certa forma boa e próxima",
            "relationship_mother": "Próxima",
            "relationship_family_members": "Difícil, principalmente com parentes distântes",
            "expectations_childhood_education": "Expectativas de melhorar o comportamento dele"
        }
        """
        return self._create_anamnesis(request, *args, **kwargs)

    def retrieve(self, request, pk, *args, **kwargs):
        """
        GET data an especific monitoring sheet.
        """
        return super().retrieve(request, pk, *args, **kwargs)

    def partial_update(self, request, pk, *args, **kwargs):
        """
        PUT data an specific monitoring sheet.
        """
        return super().partial_update(request, pk, *args, **kwargs)



class MonitoringSheetModelViewset(viewsets.ModelViewSet):
    queryset = MonitoringSheetModels.objects.all().order_by("-created_at")
    http_method_names = ["get", "retrieve", "post", "patch", "options"]

    SERIALIZER_ACTION = {
        "create": CreateMonitoringSheetSerializer,
        "list": MonitoringSheetSerializer,
        "retrieve": MonitoringSheetSerializer,
        "partial_update": MonitoringSheetSerializer,
        "update": ...,
        "destroy": ...,
    }

    def get_serializer_class(self):
        """
        GET appropriate serializer for the action.
        """

        action = self.action

        return self.SERIALIZER_ACTION[action]

    def _create_monitoring_sheet(self, request, *args, **kwargs):
        logging.info("Creating a new monitoring sheet...")

        logging.info("Starting serializer data...")
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)

        if not serializer.is_valid():
            logging.warning("Something happened in validation... %s", serializer.errors)
            raise MonitoringSheetException(serializer.errors)

        self.perform_create(serializer=serializer)

        return Response(status=HTTP_201_CREATED)

    def create(self, request, *args, **kwargs) -> Response:
        """
        Create new Monitoring sheet.

        Exemple HTTP POST payload:
        {
            name: str,
            birthday: date,
            phone_number: str(51999999999),
            telephone_number str(5199999999),
            cep: str,
            address: str,
            neighborhood: str,
            state: str,
            city: str,
            sex: str,
            recommendation: str,
            entry_date: date,
            specialist_monitoring: str,
            head_teacher: str,
            extra_information: str
        }
        """
        return self._create_monitoring_sheet(request, *args, **kwargs)

    def retrieve(self, request, pk, *args, **kwargs):
        """
        GET data an especific monitoring sheet.
        """
        return super().retrieve(request, pk, *args, **kwargs)

    def partial_update(self, request, pk, *args, **kwargs):
        """
        PATCH data an specific monitoring sheet.
        """
        return super().partial_update(request, pk, *args, **kwargs)

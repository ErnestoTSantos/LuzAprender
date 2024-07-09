from typing import Any, List, Optional, Tuple, Union

from django.contrib import admin
from django.http.request import HttpRequest

from pampulha.apps.anamnesis.models import AnamnesisModels, MonitoringSheetModels

admin.site.site_header = "Luz Aprender"


@admin.register(MonitoringSheetModels)
class MonitoringSheetAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "phone_number", "telephone_number", "gender"]
    list_filter = ["gender"]

    def get_readonly_fields(
        self, request: HttpRequest, obj: Any | None = ...
    ) -> List[str] | Tuple[Any, ...]:
        if obj:
            return [
                "id",
                "name",
                "birthday",
                "address",
                "phone_number",
                "created_at",
                "updated_at",
                "neighborhood",
                "cep",
                "state",
                "city",
                "telephone_number",
                "gender",
                "recommendation",
                "entry_date",
                "specialist_monitoring",
                "head_teacher",
                "extra_information",
            ]
        else:
            return ["id"]


@admin.register(AnamnesisModels)
class AnamnesisAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "age", "phone_number", "father", "mother"]
    list_filter = ["age"]
    fieldsets = (
        (
            "Indentificação",
            {"fields": ("id", "name", "birthday", "age", "address", "phone_number")},
        ),
        (
            "Informações do pai",
            {
                "fields": (
                    "father",
                    "father_age",
                    "father_schooling",
                    "father_profession",
                )
            },
        ),
        (
            "Informações da mãe",
            {
                "fields": (
                    "mother",
                    "mother_age",
                    "mother_schooling",
                    "mother_profession",
                )
            },
        ),
        (
            "Informações de irmãos",
            {
                "fields": (
                    "brothers_name",
                    "brothers_age",
                    "brothers_schooling",
                    "brothers_profession",
                    "birth_postion",
                )
            },
        ),
        (
            "Informações da gravidez",
            {
                "fields": (
                    "family_complaint",
                    "pregnancy_history",
                    "prenatal_care",
                    "where_was",
                    "type_of_delivery",
                    "on_the_expected_date",
                    "complications",
                )
            },
        ),
        (
            "Condições do nenê",
            {
                "fields": (
                    "color",
                    "weight",
                    "measure",
                    "needed_hospitalize",
                    "how_much_time",
                    "reason",
                    "medication",
                    "performed_surgery",
                )
            },
        ),
        (
            "Cuidados iniciais",
            {
                "fields": (
                    "first_contact_with_chest",
                    "sucking_swallowing_difficulties",
                    "when_stop_breastfeeding",
                    "used_bottle",
                    "used_acifier",
                )
            },
        ),
        (
            "Alimentação",
            {
                "fields": (
                    "start_solid_food",
                    "reactions",
                    "had_eating_difficulties",
                    "current_power",
                )
            },
        ),
        (
            "Sono",
            {
                "fields": (
                    "shared_bed",
                    "sleep",
                    "wake_up",
                    "sleeping_rituals",
                    "currently_sleep",
                )
            },
        ),
        (
            "Comunicação",
            {
                "fields": (
                    "first_speech",
                    "accompanied",
                    "currently_speak",
                    "language_disorders",
                    "other_media",
                )
            },
        ),
        (
            "Morticidade",
            {
                "fields": (
                    "sat",
                    "crawled",
                    "start_walk",
                    "fence_walker",
                    "tendency_fall",
                    "accidents",
                    "swings_other_movements",
                    "father_presence_absence",
                    "mother_conduct",
                )
            },
        ),
        (
            "Controle Esfincteriano",
            {"fields": ("removal_diapers", "nocturnal_enuresis", "encomprese")},
        ),
        (
            "Histórico de brincar",
            {
                "fields": (
                    "who_play_with",
                    "how_play",
                    "favorite_toys_games",
                    "attitudes_towards_toys",
                    "start_drawing",
                    "conduct",
                ),
            },
        ),
        (
            "Características pessoais",
            {
                "fields": (
                    "curious",
                    "observer",
                    "happy",
                    "good_memory",
                    "aggressive",
                    "stubborn",
                    "make_friends",
                    "affective",
                    "withdrawn",
                    "dependent",
                    "changeable_mood",
                    "reaction_upset",
                    "relationship_father",
                    "relationship_mother",
                    "relationship_family_members",
                    "expectations_childhood_education",
                    "other_observations",
                ),
            },
        ),
    )

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context.update(
            {
                "show_save_and_continue": False,
                "show_save_and_add_another": False,
                "show_save": False,
                "show_delete": False,
            }
        )
        return super().change_view(
            request, object_id, form_url, extra_context=extra_context,
        )

    def get_readonly_fields(
        self, request: HttpRequest, obj: Any | None = ...
    ) -> List[str] | Tuple[Any, ...]:
        if obj:
            return [
                "id",
                "name",
                "birthday",
                "age",
                "address",
                "phone_number",
                "father",
                "father_age",
                "father_schooling",
                "father_profession",
                "mother",
                "mother_age",
                "mother_schooling",
                "mother_profession",
                "brothers_name",
                "brothers_age",
                "brothers_schooling",
                "brothers_profession",
                "birth_postion",
                "family_complaint",
                "pregnancy_history",
                "prenatal_care",
                "where_was",
                "type_of_delivery",
                "on_the_expected_date",
                "complications",
                "color",
                "weight",
                "measure",
                "needed_hospitalize",
                "how_much_time",
                "reason",
                "medication",
                "performed_surgery",
                "First_contact_with_chest",
                "sucking_swallowing_difficulties",
                "when_stop_breastfeeding",
                "used_bottle",
                "used_acifier",
                "start_solid_food",
                "reactions",
                "had_eating_difficulties",
                "current_power",
                "shared_bed",
                "sleep",
                "wake_up",
                "sleeping_rituals",
                "currently_sleep",
                "first_speech",
                "accompanied",
                "currently_speak",
                "language_disorders",
                "other_media",
                "sat",
                "crawled",
                "start_walk",
                "fence_walker",
                "tendency_fall",
                "accidents",
                "swings_other_movements",
                "father_presence_absence",
                "mother_conduct",
                "removal_diapers",
                "nocturnal_enuresis",
                "encomprese",
                "who_play_with",
                "how_play",
                "favorite_toys_games",
                "attitudes_towards_toys",
                "start_drawing",
                "conduct",
                "curious",
                "observer",
                "happy",
                "good_memory",
                "aggressive",
                "stubborn",
                "make_friends",
                "affective",
                "withdrawn",
                "dependent",
                "changeable_mood",
                "reaction_upset",
                "relationship_father",
                "relationship_mother",
                "relationship_family_members",
                "expectations_childhood_education",
                "other_observations",
            ]
        else:
            return ["id"]

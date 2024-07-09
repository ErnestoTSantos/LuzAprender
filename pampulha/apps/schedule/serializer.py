from rest_framework import serializers

from pampulha.apps.schedule.models import CalendarModel
from pampulha.apps.users.models import PsychologistModel


class calendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarModel
        exclude = (
            "created_at",
            "update_at",
        )

    def create(self, validated_data):
        return CalendarModel.objects.create(**validated_data)

from django.contrib import admin

from pampulha.apps.users.models import PsychologistModel


@admin.register(PsychologistModel)
class PsychologistAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "user_data", "created_at")
    list_per_page = 10

    def get_readonly_fields(self, request, obj):
        if obj:
            return [
                "id",
                "username",
                "password",
                "created_at",
                "updated_at",
                "user_data",
            ]
        else:
            return ["id", "created_at", "updated_at"]

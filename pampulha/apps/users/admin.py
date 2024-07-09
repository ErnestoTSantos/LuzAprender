from django.contrib import admin

from pampulha.apps.users.models import PsychologistModel


@admin.register(PsychologistModel)
class PsychologistAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "created_at")
    readonly_fields = ("id", "username", "password")
    list_per_page = 10

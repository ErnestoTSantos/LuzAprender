from django.contrib import admin

from pampulha.apps.schedule.models import CalendarModel


@admin.register(CalendarModel)
class CalendarAdmin(admin.ModelAdmin):
    fields = ["id", "title", "date"]

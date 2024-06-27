import uuid

from django.db import models


class CalendarModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField("Título", max_length=50)
    date = models.DateTimeField("Dia e hora do compromisso")
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    description = models.TextField("Informações do compromisso", blank=True)

    def __str__(self) -> str:
        return f"Commitment: {self.id}"

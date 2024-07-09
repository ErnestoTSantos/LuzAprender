import uuid

from django.contrib.auth.hashers import make_password
from django.db import models


class PsychologistModel(models.Model):
    class GenderChoices(models.TextChoices):
        MALE = "M", "Masculino"
        FEMALE = "F", "Feminino"

    id = models.UUIDField("Identificador do usuário", default=uuid.uuid4, primary_key=True)
    username = models.CharField("Username", max_length=255, null=False, unique=True)
    password = models.CharField("Password", max_length=255, null=False)
    name = models.CharField("Nome", max_length=255, null=False)
    age = models.IntegerField("Idade", null=False)
    gender = models.CharField("Gênero", choices=GenderChoices.choices, max_length=15, null=False)
    created_at = models.DateField("Creation date", auto_now_add=True, editable=False)
    updated_at = models.DateField("Updated date", auto_now=True, editable=False)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(PsychologistModel, self).save(*args, **kwargs)

    def get_gender_display(self):
        return self.GenderChoices(self.gender).label

    class Meta:
        verbose_name = "Psychologist"
        verbose_name_plural = "Psychologists"

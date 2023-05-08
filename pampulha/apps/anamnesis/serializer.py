import re
from typing import Optional

from rest_framework.serializers import (
    ChoiceField,
    JSONField,
    ModelSerializer,
    ValidationError,
)

from pampulha.apps.anamnesis.models import AnamnesisModels, MonitoringSheetModels
from pampulha.apps.anamnesis.utils import Verification


class MonitoringSheetSerializer(ModelSerializer):
    class Meta:
        model = MonitoringSheetModels
        fields = (
            "id",
            "name",
            "birthday",
            "address",
            "phone_number",
            "cep",
            "state",
            "neighborhood",
            "city",
            "telephone_number",
            "sex",
            "recommendation",
            "entry_date",
            "specialist_monitoring",
            "head_teacher",
            "extra_information",
        )


class CreateMonitoringSheetSerializer(ModelSerializer):
    SEX = (("Masculino"), ("Feminino"))

    sex = ChoiceField(required=True, choices=SEX)

    class Meta:
        model = MonitoringSheetModels
        fields = "__all__"

    def validate_sex(self, sex: str) -> str:
        if sex == "Masculino":
            return "Male"

        return "Female"

    def validate_name(self, name: str) -> str:
        if " " not in name:
            raise ValidationError("Name must have a last name.")

        if len(name) < 7:
            raise ValidationError("The name is too short.")

        return name

    def validate_phone_number(self, phone_number: str) -> str:
        verification_numbers = re.sub(r"[^0-9]", "", phone_number)
        amount_characters_phone = len(phone_number)

        if amount_characters_phone < 11 or amount_characters_phone > 13:
            raise ValidationError(
                "The phone number must have a minimum of 11 digits and a maximum of 13."
            )

        if phone_number != verification_numbers:
            raise ValidationError("The number can only have values between 0-9.")

        if phone_number.startswith("55"):
            return phone_number

        return f"55{phone_number}"

    def validate_telephone_number(self, telephone_number: str) -> Optional[str]:
        if telephone_number is None:
            return telephone_number

        verification_numbers = re.sub(r"[^0-9]", "", telephone_number)
        amount_characters_phone = len(telephone_number)

        if amount_characters_phone < 8 or amount_characters_phone > 10:
            raise ValidationError(
                "The telephone number must have a minimum of 8 digits and a maximum of 10."
            )

        if telephone_number != verification_numbers:
            raise ValidationError("The number can only have values between 0-9.")

        return telephone_number

    def validate(self, data: dict) -> dict:
        cep = data.get("cep", "")

        (
            validate_cep,
            validate_state,
            validate_city,
            validate_neighborhood,
            validate_address,
        ) = Verification.verificate_cep(cep=cep)

        if not validate_cep:
            raise ValidationError("Cep not found!")

        if validate_cep != cep:
            raise ValidationError("Invalid residence information.")

        data["state"] = validate_state
        data["address"] = validate_address
        data["city"] = validate_city
        data["neighborhood"] = validate_neighborhood

        return data


class AnamnesisSerializer(ModelSerializer):
    class Meta:
        model = AnamnesisModels
        exclude = (
            "created_at",
            "updated_at",
        )


class CreateAnamnesisSerializer(ModelSerializer):
    class Meta:
        model = AnamnesisModels
        fields = "__all__"

    def validate_name(self, name: str) -> str:
        if " " not in name:
            raise ValidationError("Name must have a last name.")

        if len(name) < 7:
            raise ValidationError("The name is too short.")

        return name

    def validate_phone_number(self, phone_number: str) -> str:
        verification_numbers = re.sub(r"[^0-9]", "", phone_number)
        amount_characters_phone = len(phone_number)

        if amount_characters_phone < 11 or amount_characters_phone > 13:
            raise ValidationError(
                "The phone number must have a minimum of 11 digits and a maximum of 13."
            )

        if phone_number != verification_numbers:
            raise ValidationError("The number can only have values between 0-9.")

        if phone_number.startswith("55"):
            return phone_number

        return f"55{phone_number}"

    def validate_age(self, age: int) -> int:
        if age < 0:
            raise ValidationError("Age cannot be less than 0.")

        return age

    def validate_father(self, father: str) -> str:
        if " " not in father:
            raise ValidationError("Father name must have a last name.")

        if len(father) < 7:
            raise ValidationError("The father name is too short.")

        return father

    def validate_mother(self, mother: str) -> str:
        if " " not in mother:
            raise ValidationError("Mother name must have a last name.")

        if len(mother) < 7:
            raise ValidationError("The mother name is too short.")

        return mother

    def validate_father_age(self, father_age: int) -> int:
        if father_age < 0:
            raise ValidationError("Father age cannot be less than 0.")

        return father_age

    def validate_mother_age(self, mother_age: int) -> int:
        if mother_age < 0:
            raise ValidationError("Mother age cannot be less than 0.")

        return mother_age

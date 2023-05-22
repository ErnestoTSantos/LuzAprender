import uuid

from django.db import models


class BaseFileModels(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField("Nome", max_length=255)
    birthday = models.DateField("Aniversário")
    address = models.CharField("Endereço", max_length=255)
    phone_number = models.CharField("Número de contato", max_length=13)
    created_at = models.DateField("Criado em", auto_now_add=True)
    updated_at = models.DateField("Atualizado em", auto_now=True)


class MonitoringSheetModels(BaseFileModels):
    SEX = (("Male", "Masculino"), ("Female", "Feminino"))

    neighborhood = models.CharField("Bairro", max_length=255)
    cep = models.CharField("CEP", max_length=10)
    state = models.CharField("Estado", max_length=255)
    city = models.CharField("Cidade", max_length=255)
    telephone_number = models.CharField(
        "Telefone", max_length=10, null=True, blank=True
    )
    sex = models.CharField("Sexo", choices=SEX, max_length=6)
    recommendation = models.BooleanField("Recomendação", default=False)
    entry_date = models.DateField("Data de entrada")
    specialist_monitoring = models.CharField(
        "Acompanhamento com outros especialistas", max_length=255, null=True, blank=True
    )
    head_teacher = models.CharField(
        "Professora títular", max_length=255, null=True, blank=True
    )
    extra_information = models.TextField("Anotações", null=True, blank=True)

    def __str__(self):
        return f"<Monitoring Sheet: {self.id}>"

    class Meta:
        verbose_name = "Monitoring Sheet"
        verbose_name_plural = "Monitoring Sheets"


class AnamnesisModels(BaseFileModels):
    # Identification data
    age = models.IntegerField("Idade")

    # Father informations
    father = models.CharField("Pai", max_length=255, null=True, blank=True)
    father_age = models.IntegerField("Idade", null=True, blank=True)
    father_schooling = models.CharField(
        "Escolaridade", max_length=255, null=True, blank=True
    )
    father_profession = models.CharField(
        "Profissão", max_length=255, null=True, blank=True
    )

    # Mother informations
    mother = models.CharField("Mãe", max_length=255, null=True, blank=True)
    mother_age = models.IntegerField("Idade", null=True, blank=True)
    mother_schooling = models.CharField(
        "Escolaridade", max_length=255, null=True, blank=True
    )
    mother_profession = models.CharField(
        "Profissão", max_length=255, null=True, blank=True
    )

    # Brothers informations
    brothers_name = models.JSONField(
        "Nome dos irmãos", default=dict, null=True, blank=True
    )
    brothers_age = models.JSONField(
        "Idade dos irmãos", default=dict, null=True, blank=True
    )
    brothers_schooling = models.JSONField(
        "Escolaridade", default=dict, null=True, blank=True
    )
    brothers_profession = models.JSONField(
        "Profissão", default=dict, null=True, blank=True
    )
    birth_postion = models.CharField(
        "Identificar se é filho mais velho, mais novo, do meio...",
        max_length=255,
        null=True,
        blank=True,
    )

    # Pregnancy information
    family_complaint = models.TextField("Queixa familiar")
    pregnancy_history = models.TextField("Como aconteceu")
    prenatal_care = models.TextField("Acompanhamento pré natal")
    where_was = models.CharField("Onde foi", max_length=255)
    type_of_delivery = models.CharField("Tipo de parto", max_length=255)
    on_the_expected_date = models.BooleanField("Na data esperada", default=True)
    complications = models.CharField("Complicações", max_length=255)

    # Conditions of the newborn
    color = models.CharField("Cor do nascimento", max_length=255)
    weight = models.FloatField("Peso")
    measure = models.FloatField("Medida")
    needed_hospitalize = models.CharField("Precisou hospitalizar", max_length=50)
    how_much_time = models.CharField(
        "Quanto tempo", max_length=50, null=True, blank=True
    )
    reason = models.CharField("Razão", max_length=100, null=True, blank=True)
    medication = models.CharField("Medicação", max_length=100, null=True, blank=True)
    performed_surgery = models.CharField(
        "Cirurgia necessária", max_length=200, null=True, blank=True
    )

    # Nursing
    First_contact_with_chest = models.CharField(
        "Primeiro contato com o peito", max_length=50
    )
    sucking_swallowing_difficulties = models.BooleanField(
        "Dificuldades com amamentação", default=False
    )
    when_stop_breastfeeding = models.CharField(
        "Quando deixou de mamar no peito", max_length=50
    )
    used_bottle = models.BooleanField("Usou mamadeira", default=True)
    used_acifier = models.BooleanField("Usou chupeta", default=True)

    # Food
    start_solid_food = models.CharField("Incio da alimentação sólida", max_length=50)
    reactions = models.TextField("Reações")
    had_eating_difficulties = models.CharField(
        "Dificuldades para alimentar", max_length=200
    )
    current_power = models.CharField("Como se alimenta atualmente", max_length=200)

    # Sleep
    shared_bed = models.BooleanField("Compartilha leito", default=True)
    sleep = models.CharField("Como dormia", max_length=200)
    wake_up = models.CharField("Como acordava", max_length=200)
    sleeping_rituals = models.CharField("Rituais para dormir", max_length=255)
    currently_sleep = models.CharField("Como dorme atualmente", max_length=255)

    # Language
    first_speech = models.CharField(
        "Quando pronunciou a primeira palavra", max_length=255
    )
    accompanied = models.CharField("Quem acompanhou", max_length=255)
    currently_speak = models.CharField("Como fala atualmente", max_length=255)
    language_disorders = models.CharField(
        "Outras maneiras de comunicar", max_length=255
    )
    other_media = models.TextField("Outros meios de comunicação", null=True, blank=True)

    # Motricity
    sat = models.CharField("Quando sentou", max_length=50)
    crawled = models.CharField("Como e quando engatinhou", max_length=255)
    start_walk = models.CharField("Quando e como começou a caminhar", max_length=255)
    fence_walker = models.CharField("Usou cercado e andador", max_length=255)
    tendency_fall = models.CharField("Tendência a cair", max_length=50)
    accidents = models.CharField("Acidentes", max_length=255)
    swings_other_movements = models.CharField(
        "Balanços e outros movimentos", max_length=255
    )
    father_presence_absence = models.CharField(
        "Presença ou ausência do pai nesse período", max_length=255
    )
    mother_conduct = models.CharField("Conduta da mãe", max_length=255)

    # Sphinterial Control
    removal_diapers = models.CharField("Como foi a retirada de fraldas", max_length=255)
    nocturnal_enuresis = models.CharField("Tem enurese noturna", max_length=255)
    encomprese = models.CharField("Encomprese", max_length=255)

    # Playful Biography
    who_play_with = models.CharField("Com quem brinca", max_length=255)
    how_play = models.CharField("Como brinca", max_length=255)
    favorite_toys_games = models.CharField(
        "Brinquedos e brincadeiras preferidas", max_length=255
    )
    attitudes_towards_toys = models.CharField(
        "Atitudes frente aos brinquedos", max_length=255
    )
    start_drawing = models.CharField("Quando começou a desenhar", max_length=255)
    conduct = models.CharField("Conduta", max_length=255)

    # Personal characteristics
    curious = models.BooleanField("Curioso/a")
    observer = models.BooleanField("Observador/a")
    happy = models.BooleanField("Alegre")
    good_memory = models.BooleanField("Boa memória")
    aggressive = models.BooleanField("Agressivo/a")
    stubborn = models.BooleanField("Teimoso/a")
    make_friends = models.BooleanField("Faz amizades")
    affective = models.BooleanField("Afetivo/a")
    withdrawn = models.BooleanField("Retraído/a")
    dependent = models.BooleanField("Dependente")
    changeable_mood = models.BooleanField("Humor variável")
    reaction_upset = models.CharField(
        "Como reage, quando contrariado/a", max_length=255
    )
    relationship_father = models.CharField("Relação com o pai", max_length=255)
    relationship_mother = models.CharField("Relação com a mãe", max_length=255)
    relationship_family_members = models.CharField(
        "Relação com os demais membros da família", max_length=255
    )
    expectations_childhood_education = models.TextField(
        "Expectativas em relação ao atendimento da educação infatil"
    )
    other_observations = models.TextField("Outras observações", null=True, blank=True)

    def __str__(self):
        return f"<Anamnesis: {self.id}>"

    class Meta:
        verbose_name = "Anamnesi"
        verbose_name_plural = "Anamnesis"

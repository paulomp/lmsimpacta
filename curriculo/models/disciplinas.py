from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from contas.models import Coordenador

class Disciplina(models.Model):
    STATUS = (
        ("ABERTA", "Aberta"),
        ("FECHADA", "Fechada")
    )

    nome = models.CharField(max_length=255, unique=True)
    data = models.DateField(default=timezone.now, blank=True, null=True)
    status = models.CharField(max_length=50, default='ABERTA', blank=True, null=True, choices=STATUS)
    plano_ensino = models.TextField(max_length=500)
    carga_horaria = models.IntegerField()
    competencias = models.TextField(max_length=500)
    habilidades = models.TextField(max_length=500)
    ementa = models.TextField(max_length=500)
    conteudo_programatico = models.TextField(max_length=500)
    bibliografia_basica = models.TextField(max_length=500)
    bibliografia_complementar = models.TextField(max_length=500)
    percentual_pratico = models.IntegerField()
    percentual_teorico = models.IntegerField()
    coordenador = models.ForeignKey(Coordenador, models.PROTECT)

    def __str__(self):
        return self.nome

    def clean(self):
        if self.percentual_teorico > 100 or self.percentual_teorico < 0:
            raise ValidationError('O percentual teórico deve estar entre 0 e 100.')
        if self.percentual_pratico > 100 or self.percentual_pratico < 0:
            raise ValidationError('O percentual prático  deve estar entre 0 e 100.')
        if self.percentual_teorico + self.percentual_pratico != 100:
            raise ValidationError('A soma das porcentagens deve ser igual a 100')
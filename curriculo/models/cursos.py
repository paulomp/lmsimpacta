from django.db import models
from curriculo.models.disciplinas import Disciplina


class Curso(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    sigla = models.CharField(max_length=5, unique=True)
    disciplinas = models.ManyToManyField(Disciplina, through='MatrizCurricular')

    def __str__(self):
        return self.nome

class MatrizCurricular(models.Model):

    semestre = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.SET_NULL, null=True)
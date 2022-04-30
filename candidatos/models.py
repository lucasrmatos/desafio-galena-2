from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models
from phone_field import PhoneField
from cpf_field.models import CPFField

class Candidato(models.Model):

    email = models.EmailField(max_length=30)
    nome = models.CharField(max_length=30)
    grupo = models.PositiveIntegerField()
    nome_do_grupo = models.CharField(max_length=30)
    cpf = CPFField('cpf')
    telefone = PhoneField(blank=True, help_text='celular')
    data_Nascto = models.DateField()
    endereço = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
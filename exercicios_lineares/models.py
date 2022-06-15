from django.db import models


class Exercicio(models.Model):
    fator1 = models.TextField(max_length=5)
    fator2 = models.TextField(max_length=5)
    operador = models.TextField(max_length=1)

    class Meta:
        verbose_name = 'Exercicio'
        verbose_name_plural = 'Exercicios'

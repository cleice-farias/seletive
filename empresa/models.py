from django.db import models


class empresa(models.Model):
    nome = models.CharField(max_length=60)
    email = models.EmailField()
    cidade = models.CharField(max_length=60)
    endereco = models.CharField(max_length=120)
    nicho_mercado = models.CharField(max_length=30)
    caracteristica_empresa = models.TextField()


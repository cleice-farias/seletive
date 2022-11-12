from django.db import models


class empresa(models.Model):
    nome = models.CharField(max_length=60)
    email = models.EmailField()
    cidade = models.CharField(max_length=60)
    endereco = models.CharField(max_length=120)
    nicho_mercado = models.CharField(max_length=10, choices=[('T', 'Tecnologia'), ('A', 'Administraçao'), ('D', 'Design'), ('M', 'Marketing')])
    caracteristica_empresa = models.TextField()

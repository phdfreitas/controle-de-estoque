from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Produto(models.Model):
    STATUS = (('disponível', 'Disponível'), ('indisponível', 'Indisponível'))
    nome = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100)
    marca = models.CharField(max_length=50)
    descricao = models.TextField()
    quantidade = models.IntegerField()
    preco = models.CharField(max_length=6)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # Mostrará o usuário que fez o cadastro do produto
    cadastrado = models.DateTimeField(auto_now_add=True) # Só é alterado no momento do cadastro do produto
    alterado = models.DateTimeField(auto_now=True) # Salvará a data e hora em que sofrer alguma alteração
    status = models.CharField(max_length=12, choices=STATUS, default='indisponível')

    def __str__(self):
        return self.nome
from django.db import models
from django.dispatch import receiver
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Produto(models.Model):
    STATUS = (('Disponível', 'Disponível'), ('Indisponível', 'Indisponível'))
    nome = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100)
    descricao = models.TextField()
    quantidade = models.IntegerField()
    preco = models.CharField(max_length=10)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # Mostrará o usuário que fez o cadastro do produto
    cadastrado = models.DateTimeField(default=timezone.now) # Só é alterado no momento do cadastro do produto
    alterado = models.DateTimeField(auto_now=True) # Salvará a data e hora em que sofrer alguma alteração
    status = models.CharField(max_length=12, choices=STATUS, default='Disponível')

    def get_absolute_url(self):
        return reverse('detalharProduto', args=[self.slug])

    def get_absolute_url_update(self):
        return reverse('atualizarProduto', args=[self.slug])

    def get_absolute_url_delete(self):
        return reverse('excluirProduto', args=[self.slug])

    class Meta:
        ordering = ('cadastrado',)

    def __str__(self):
        return self.nome

@receiver(post_save, sender=Produto)
def insert_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(f'produto-{instance.marca}-{instance.nome}')
        return instance.save()
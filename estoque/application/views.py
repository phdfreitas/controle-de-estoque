from django.shortcuts import render
from django.views.generic import ListView
from . models import Produto

class ProdutoListView(ListView):
    model = Produto
    template_name = 'produto/listar-produto.html'
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Produto


class ProdutoListView(ListView):
    model = Produto
    template_name = 'produto/listar-produto.html'


class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produto/detalhar-produto.html'
    context_object_name = 'produto'
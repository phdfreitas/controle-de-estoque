from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView
from . models import Produto


class ProdutoListView(ListView):
    model = Produto
    template_name = 'produto/listar-produto.html'


class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produto/detalhar-produto.html'
    context_object_name = 'produto'


class ProdutoCreateView(CreateView):
    model = Produto
    fields = ['nome', 'marca', 'descricao', 'quantidade', 'preco', 'usuario', 'status']
    template_name = 'produto/cadastrar-produto.html'


class ProdutoUpdateView(UpdateView):
    model = Produto
    fields = ['descricao', 'quantidade', 'preco', 'status']
    template_name = 'produto/atualizar-produto.html'
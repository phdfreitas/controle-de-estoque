from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from . models import Produto


class ProdutoListView(ListView):
    model = Produto
    template_name = 'produto/listar-produto.html'


class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produto/detalhar-produto.html'
    context_object_name = 'produto'


class ProdutoCreateView(SuccessMessageMixin, CreateView):
    model = Produto
    fields = '__all__'
    template_name = 'produto/cadastrar-produto.html'
    success_message = "%(field)s cadastrado com sucesso."

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.nome,
        )


class ProdutoUpdateView(SuccessMessageMixin, UpdateView):
    model = Produto
    fields = ['descricao', 'quantidade', 'preco', 'status']
    template_name = 'produto/atualizar-produto.html'
    success_message = "%(field)s atualizado com sucesso."

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.nome,
        )


class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produto/excluir-produto.html'
    success_url = reverse_lazy('listarProdutos')

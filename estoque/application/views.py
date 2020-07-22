from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin

from . models import Produto
from . filters import ProdutoFilterSet


class HomeView(TemplateView):
    template_name = 'produto/home.html'


class ProdutoListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')

    model = Produto
    template_name = 'produto/listar-produto.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProdutoFilterSet(self.request.GET, queryset=self.get_queryset())
        return context


class ProdutoDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')

    model = Produto
    template_name = 'produto/detalhar-produto.html'
    context_object_name = 'produto'


class ProdutoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')

    model = Produto
    fields = ['nome', 'marca', 'descricao', 'quantidade', 'preco', 'status']
    template_name = 'produto/cadastrar-produto.html'
    success_message = "%(field)s cadastrado com sucesso."

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.nome,
        )

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)

        return url


class ProdutoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')

    model = Produto
    fields = ['descricao', 'quantidade', 'preco', 'status']
    template_name = 'produto/atualizar-produto.html'
    success_message = "%(field)s atualizado com sucesso."

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.nome,
        )


class ProdutoDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')

    model = Produto
    template_name = 'produto/excluir-produto.html'
    success_url = reverse_lazy('listarProdutos')

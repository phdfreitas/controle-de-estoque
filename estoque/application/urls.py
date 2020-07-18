from django.urls import path
from . import views


urlpatterns = [
    path('listaProdutos', views.ProdutoListView.as_view(), name='listarProdutos'),
    path('novoProduto', views.ProdutoCreateView.as_view(), name='cadastrarProduto'),
    path('<slug:slug>/detalhes', views.ProdutoDetailView.as_view(), name='detalharProduto'),
    path('<slug:slug>/atualizar', views.ProdutoUpdateView.as_view(), name='atualizarProduto'),
    path('<slug:slug>/excluir', views.ProdutoDeleteView.as_view(), name='excluirProduto'),
]
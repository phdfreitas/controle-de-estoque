from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProdutoListView.as_view(), name='listarProdutos'),
    path('<slug:slug>', views.ProdutoDetailView.as_view(), name='detalharProduto'),
]
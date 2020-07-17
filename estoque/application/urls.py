from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProdutoListView.as_view(), name='listarProdutos'),
]
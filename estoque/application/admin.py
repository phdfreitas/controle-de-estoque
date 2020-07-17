from django.contrib import admin
from . models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin): # Permite a customizar o painel de admin
    list_display = ('nome', 'marca', 'quantidade', 'cadastrado', 'preco', 'status')
    list_filter = ('status', 'marca', 'preco') # Habilita o filtro
    date_hierarchy = 'cadastrado'
    search_fields = ('nome', 'descricao') # Habilita a pesquisa dos campos no painel admin
    prepopulated_fields = {'slug':('marca', 'nome')} # "Cria" o slug baseado na marca e no nome
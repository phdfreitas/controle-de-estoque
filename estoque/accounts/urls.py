from django.urls import path
from . import views


urlpatterns = [
    path('cadastrar', views.CadastrarNovoUsuario.as_view(), name='cadastrarUsuario'),
]
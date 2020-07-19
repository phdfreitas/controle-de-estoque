import django_filters as filter
from . models import Produto


class ProdutoFilterSet(filter.FilterSet):
    class Meta:
        model = Produto
        fields = {
            'nome': ['icontains'],
            'marca': ['icontains'],
            'status': ['contains'],
        }

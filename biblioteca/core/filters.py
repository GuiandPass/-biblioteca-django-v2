from django_filters import rest_framework as filters
from .models import Livro

class LivroFilter(filters.FilterSet):
    titulo = filters.CharFilter(lookup_expr='icontains')
    autor = filters.CharFilter(field_name='autor__nome', lookup_expr='icontains')
    categoria = filters.AllValuesFilter(field_name='categoria__nome')
    
    nome_categoria = filters.CharFilter(field_name='categoria__nome', lookup_expr='startswith')  # começa com
    nome_livro = filters.CharFilter(field_name='titulo', lookup_expr='startswith')  # começa com

    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'categoria', 'nome_categoria', 'nome_livro']
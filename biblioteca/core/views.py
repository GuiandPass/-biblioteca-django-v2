from rest_framework import generics
from .models import Livro, Categoria, Autor
from .serializers import LivroSerializer, CategoriaSerializer, AutorSerializer
from .filters import LivroFilter

# Class-based view para listar e criar livros
class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filterset_class = LivroFilter
    ordering_fields = ['titulo', 'autor', 'categoria', 'publicado_em']
    ordering = ['titulo']
    name = "livro-list"

# Class-based view para obter, atualizar e deletar um livro específico
class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = "livro-detail"

# Class-based view para listar e criar categorias
class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = "categoria-list"
    ordering_fields = ['nome'] 
    ordering = ['nome']

# Class-based view para obter, atualizar e deletar uma categoria específica
class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = "categoria-detail"

# Class-based view para listar e criar autores
class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = "autor-list"
    ordering_fields = ['nome']
    ordering = ['nome']

# Class-based view para obter, atualizar e deletar um autor específico
class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = "autor-detail"

import django_filters
from .models import Produto    

class FilterProduto(django_filters.FilterSet):                           
    nome = django_filters.CharFilter(lookup_expr='icontains')          
    class Meta:
        model = Produto
        fields = ['nome']
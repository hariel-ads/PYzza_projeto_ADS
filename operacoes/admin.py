from django.contrib import admin
from .models import (
    Fornecedor, 
    RegistroEntrada, 
    ProdutoEntrada,
    RegistroSaida, 
    ProdutoSaida
)

admin.site.register(Fornecedor)
admin.site.register(RegistroEntrada)
admin.site.register(ProdutoEntrada)
admin.site.register(RegistroSaida)
admin.site.register(ProdutoSaida)
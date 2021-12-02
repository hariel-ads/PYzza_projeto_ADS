from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('fornecedores/', views.ViewListaFornecedor.as_view(), name='lista-fornecedores'),
    path('fornecedores/novo', views.ViewNovoFornecedor.as_view(), name='novo-fornecedor'),
    path('fornecedores/<pk>/editar', views.ViewAtualizarFornecedor.as_view(), name='editar-fornecedor'),
    path('fornecedores/<pk>/deletar', views.ViewDeletarFornecedor.as_view(), name='deletar-fornecedor'),
    path('fornecedores/<nome>', views.ViewFornecedor.as_view(), name='fornecedor'),

    path('entradas/', views.ViewEntradas.as_view(), name='lista-entradas'), 
    path('entradas/novo', views.ViewSelecionaFornecedor.as_view(), name='selecionar-fornecedor'), 
    path('entradas/novo/<pk>', views.ViewNovaEntrada.as_view(), name='nova-entrada'),    
    path('entradas/<pk>/deletar', views.ViewDeletarEntrada.as_view(), name='deletar-entrada'),
    
    path('saidas/', views.ViewSaida.as_view(), name='lista-saidas'),
    path('saidas/novo', views.ViewNovaSaida.as_view(), name='nova-saida'),
    path('saidas/<pk>/deletar', views.ViewDeletarSaida.as_view(), name='deletar-saida'),

    path("entradas/<registro>", views.ViewRegistroEntrada.as_view(), name="registro-entrada"),
    path("saidas/<registro>", views.ViewRegistroSaida.as_view(), name="registro-saida"),
]
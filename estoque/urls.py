from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.ViewListaProduto.as_view(), name='estoque'),
    path('new', views.ViewNovoProduto.as_view(), name='novo-produto'),
    path('estoque/<pk>/editar', views.ViewAtualizarProduto.as_view(), name='editar-produto'),
    path('estoque/<pk>/deletar', views.ViewDeletarProduto.as_view(), name='deletar-produto'),
]
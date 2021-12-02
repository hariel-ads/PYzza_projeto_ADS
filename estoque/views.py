from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    View,
    CreateView, 
    UpdateView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Produto
from .forms import FormProduto
from django_filters.views import FilterView
from .filters import FilterProduto


class ViewListaProduto(FilterView):
    filterset_class = FilterProduto
    queryset = Produto.objects.filter(is_deleted=False)
    template_name = 'estoque.html'
    paginate_by = 10


class ViewNovoProduto(SuccessMessageMixin, CreateView):                                 
    model = Produto                                                                       
    form_class = FormProduto                                                            
    template_name = "editar_produto.html"                                                 
    success_url = '/estoque'                                                         
    success_message = "Produto adicionado com sucesso"                             

    def get_context_data(self, **kwargs):                                              
        context = super().get_context_data(**kwargs)
        context["title"] = 'Novo Produto'
        context["savebtn"] = 'Adicionar ao Estoque'
        return context       


class ViewAtualizarProduto(SuccessMessageMixin, UpdateView):                               
    model = Produto                                                                     
    form_class = FormProduto                                                              
    template_name = "editar_produto.html"                                               
    success_url = '/estoque'                                                       
    success_message = "Produto adicionado com sucesso"                            

    def get_context_data(self, **kwargs):                                            
        context = super().get_context_data(**kwargs)
        context["title"] = 'Editar Produto'
        context["savebtn"] = 'Atualizar Produto'
        context["delbtn"] = 'Deletar Produto'
        return context


class ViewDeletarProduto(View):                                                          
    template_name = "deletar_produto.html"                                                
    success_message = "Produto deletado com sucesso"                            
    
    def get(self, request, pk):
        produto = get_object_or_404(Produto, pk=pk)
        return render(request, self.template_name, {'object' : produto})

    def post(self, request, pk):  
        produto = get_object_or_404(Produto, pk=pk)
        produto.is_deleted = True
        produto.save()                                               
        messages.success(request, self.success_message)
        return redirect('estoque')
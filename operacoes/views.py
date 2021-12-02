from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    View, 
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import (
    RegistroEntrada, 
    Fornecedor, 
    ProdutoEntrada,
    RegistroSaida,  
    ProdutoSaida,
)
from .forms import (
    FormSelecionarFornecedor, 
    FormEntradaProdutoPadrao,
    FormFornecedor, 
    FormSaida,
    FormSaidaProdutoPadrao,
)
from estoque.models import Produto



class ViewListaFornecedor(ListView):
    model = Fornecedor
    template_name = "fornecedores/lista_fornecedores.html"
    queryset = Fornecedor.objects.filter(is_deleted=False)
    paginate_by = 10


class ViewNovoFornecedor(SuccessMessageMixin, CreateView):
    model = Fornecedor
    form_class = FormFornecedor
    success_url = '/operacoes/fornecedores'
    success_message = "Fornecedor adicionado com sucesso"
    template_name = "fornecedores/editar_fornecedor.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Novo Fornecedor'
        context["savebtn"] = 'Add Supplier'
        return context     


class ViewAtualizarFornecedor(SuccessMessageMixin, UpdateView):
    model = Fornecedor
    form_class = FormFornecedor
    success_url = '/operacoes/fornecedores'
    success_message = "Dados atualizados com sucesso"
    template_name = "fornecedores/editar_fornecedor.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Editar Fornecedor'
        context["savebtn"] = 'Save Changes'
        context["delbtn"] = 'Deletar Fornecedor'
        return context


class ViewDeletarFornecedor(View):
    template_name = "fornecedores/deletar_fornecedor.html"
    success_message = "Fornecedor deletado com sucesso"

    def get(self, request, pk):
        fornecedor = get_object_or_404(Fornecedor, pk=pk)
        return render(request, self.template_name, {'object' : fornecedor})

    def post(self, request, pk):  
        fornecedor = get_object_or_404(Fornecedor, pk=pk)
        fornecedor.is_deleted = True
        fornecedor.save()                                               
        messages.success(request, self.success_message)
        return redirect('lista-fornecedores')


class ViewFornecedor(View):
    def get(self, request, nome):
        objfornecedor = get_object_or_404(Fornecedor, nome=nome)
        listaregistros = RegistroEntrada.objects.filter(fornecedor=objfornecedor)
        pagina = request.GET.get('page', 1)
        constr_pagina = Paginator(listaregistros, 10)
        try:
            registros = constr_pagina.page(pagina)
        except PageNotAnInteger:
            registros = constr_pagina.page(1)
        except EmptyPage:
            registros = constr_pagina.page(constr_pagina.num_pages)
        context = {
            'fornecedor'  : objfornecedor,
            'registros'     : registros
        }
        return render(request, 'fornecedores/fornecedor.html', context)



class ViewEntradas(ListView):
    model = RegistroEntrada
    template_name = "entradas/lista_entradas.html"
    context_object_name = 'registros'
    ordering = ['-diahora']
    paginate_by = 10


class ViewSelecionaFornecedor(View):
    form_class = FormSelecionarFornecedor
    template_name = 'entradas/selecionar_fornecedor.html'

    def get(self, request, *args, **kwargs):                                   
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):                                  
        form = self.form_class(request.POST)
        if form.is_valid():
            idfornecedor = request.POST.get("fornecedor")
            fornecedor = get_object_or_404(Fornecedor, id=idfornecedor)
            return redirect('nova-entrada', fornecedor.pk)
        return render(request, self.template_name, {'form': form})


class ViewNovaEntrada(View):                                                 
    template_name = 'entradas/nova_entrada.html'

    def get(self, request, pk):
        conjuntoform = FormEntradaProdutoPadrao(request.GET or None)                    
        objfornecedor = get_object_or_404(Fornecedor, pk=pk)                       
        context = {
            'conjuntoform'   : conjuntoform,
            'fornecedor'  : objfornecedor,
        }                                                                       
        return render(request, self.template_name, context)

    def post(self, request, pk):
        conjuntoform = FormEntradaProdutoPadrao(request.POST)                            
        objfornecedor = get_object_or_404(Fornecedor, pk=pk)                      
        if conjuntoform.is_valid():            
            objregistro = RegistroEntrada(fornecedor=objfornecedor)                       
            objregistro.save()                                                    
            
            
            for form in conjuntoform:        
                registroproduto = form.save(commit=False)
                registroproduto.registro = objregistro                
                produto = get_object_or_404(Produto, nome=registroproduto.produto.nome)          
                registroproduto.precototal = registroproduto.precounitario * registroproduto.quantidade                
                produto.quantidade += registroproduto.quantidade              
                produto.save()
                registroproduto.save()
            messages.success(request, "Entrada em estoque registrada com sucesso!")
            #return redirect('registro-entrada', billno=billobj.billno)
        conjuntoform = FormEntradaProdutoPadrao(request.GET or None)
        context = {
            'conjuntoform'   : conjuntoform,
            'fornecedor'  : objfornecedor
        }
        return render(request, self.template_name, context)


class ViewDeletarEntrada(SuccessMessageMixin, DeleteView):
    model = RegistroEntrada
    template_name = "entradas/deletar_entrada.html"
    success_url = '/operacoes/entradas'
    
    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        items = ProdutoEntrada.objects.filter(registro=self.object.registro)
        for item in items:
            produto = get_object_or_404(Produto, nome=item.produto.nome)
            if produto.is_deleted == False:
                produto.quantidade -= item.quantidade
                produto.save()
        messages.success(self.request, "Registro deletado com sucesso!")
        return super(ViewDeletarEntrada, self).delete(*args, **kwargs)


class ViewSaida(ListView):
    model = RegistroSaida
    template_name = "saidas/lista_saidas.html"
    context_object_name = 'registros'
    ordering = ['-diahora']
    paginate_by = 10


class ViewNovaSaida(View):                                                      
    template_name = 'saidas/nova_saida.html'

    def get(self, request):
        form = FormSaida(request.GET or None)
        conjuntoform = FormSaidaProdutoPadrao(request.GET or None)                        
        
        produtos = Produto.objects.filter(is_deleted=False)
        context = {
            'form'      : form,
            'conjuntoform'   : conjuntoform,
            'produtos'    : produtos
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = FormSaida(request.POST)
        conjuntoform = FormSaidaProdutoPadrao(request.POST)                                 
        if form.is_valid() and conjuntoform.is_valid():            
            objregistro = form.save(commit=False)
            objregistro.save()     
            
            
            for form in conjuntoform:           
                registroproduto = form.save(commit=False)
                registroproduto.registro = objregistro         
                produto = get_object_or_404(Produto, nome=registroproduto.produto.nome)         
                registroproduto.precototal = registroproduto.precounitario * registroproduto.quantidade                
                produto.quantidade -= registroproduto.quantidade          
                produto.save()
                registroproduto.save()
            messages.success(request, "Saída de estoque registrada com sucesso!")
            #return redirect('registro-saida', billno=billobj.billno)
        form = FormSaida(request.GET or None)
        conjuntoform = FormSaidaProdutoPadrao(request.GET or None)
        context = {
            'form'      : form,
            'conjuntoform'   : conjuntoform,
        }
        return render(request, self.template_name, context)


class ViewDeletarSaida(SuccessMessageMixin, DeleteView):
    model = RegistroSaida
    template_name = "saidas/deletar_saida.html"
    success_url = '/operacoes/saidas'
    
    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        items = ProdutoSaida.objects.filter(registro=self.object.registro)
        for item in items:
            produto = get_object_or_404(Produto, nome=item.produto.nome)
            if produto.is_deleted == False:
                produto.quantidade += item.quantidade
                produto.save()
        messages.success(self.request, "Registro deletado com sucesso!")
        return super(ViewDeletarSaida, self).delete(*args, **kwargs)


class ViewRegistroEntrada(View):
    model = RegistroEntrada
    template_name = "registro/registro_entrada.html"
    base_registro = "registro/base_registro.html"

    def get(self, request, registro):
        context = {
            'registro'          : RegistroEntrada.objects.get(registro=registro),
            'items'         : ProdutoEntrada.objects.filter(registro=registro),            
            'base_registro'     : self.base_registro,
        }
        return render(request, self.template_name, context)


class ViewRegistroSaida(View):
    model = RegistroSaida
    template_name = "registro/registro_saida.html"
    base_registro = "registro/base_registro.html"
    
    def get(self, request, registro):
        context = {
            'registro'          : RegistroSaida.objects.get(registro=registro),
            'items'         : ProdutoSaida.objects.filter(registro=registro),            
            'base_registro'     : self.base_registro,
        }
        return render(request, self.template_name, context)

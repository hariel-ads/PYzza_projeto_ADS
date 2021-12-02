from django import forms
from django.forms import formset_factory
from .models import (
    Fornecedor, 
    RegistroEntrada, 
    ProdutoEntrada,
    RegistroSaida, 
    ProdutoSaida,
)
from estoque.models import Produto


class FormSelecionarFornecedor(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fornecedor'].queryset = Fornecedor.objects.filter(is_deleted=False)
        self.fields['fornecedor'].widget.attrs.update({'class': 'textinput form-control'})
    class Meta:
        model = RegistroEntrada
        fields = ['fornecedor']


class FormEntradaProduto(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['produto'].queryset = Produto.objects.filter(is_deleted=False)
        self.fields['produto'].widget.attrs.update({'class': 'textinput form-control setprice stock', 'required': 'true'})
        self.fields['quantidade'].widget.attrs.update({'class': 'textinput form-control setprice quantity', 'min': '1', 'required': 'true'})
        self.fields['precounitario'].widget.attrs.update({'class': 'textinput form-control setprice price', 'min': '0', 'required': 'true'})
    class Meta:
        model = ProdutoEntrada
        fields = ['produto', 'quantidade', 'precounitario']


FormEntradaProdutoPadrao = formset_factory(FormEntradaProduto, extra=1)


class FormFornecedor(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'textinput form-control', 'pattern' : '[a-zA-Z\s]{1,50}', 'title' : 'Apenas nomes'})
        self.fields['telefone'].widget.attrs.update({'class': 'textinput form-control', 'maxlength': '10', 'pattern' : '[0-9]{10}', 'title' : 'Apenas númers'})
        self.fields['email'].widget.attrs.update({'class': 'textinput form-control', 'pattern' : '[a-z0-9.]+@[a-z0-9]+\.[a-z]+(\.[a-z]+)?', 'title' : 'Insira um formato de email válido'})
        self.fields['cnpj'].widget.attrs.update({'class': 'textinput form-control', 'maxlength': '14', 'pattern' : '[A-Z0-9]{14}', 'title' : 'Insira um CNPJ válido'})
    class Meta:
        model = Fornecedor
        fields = ['nome', 'telefone', 'endereco', 'email', 'cnpj']
        widgets = {
            'endereco' : forms.Textarea(
                attrs = {
                    'class' : 'textinput form-control',
                    'rows'  : '4'
                }
            )
        }


class FormSaida(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'textinput form-control', 'pattern' : '[a-zA-Z\s]{1,50}', 'title' : 'Apenas nomes', 'required': 'false', 'initial': 'exemplo'})
        self.fields['telefone'].widget.attrs.update({'class': 'textinput form-control', 'maxlength': '10', 'pattern' : '[0-9]{10}', 'title' : 'Apenas números', 'required': 'false'})
        self.fields['email'].widget.attrs.update({'class': 'textinput form-control', 'required': 'false'})
        self.fields['cnpj'].widget.attrs.update({'class': 'textinput form-control', 'maxlength': '14', 'pattern' : '[A-Z0-9]{14}', 'title' : 'Insira um CNPJ válido', 'required': 'false'})
    class Meta:
        model = RegistroSaida
        fields = ['nome', 'telefone', 'endereco', 'email', 'cnpj']
        widgets = {
            'endereco' : forms.Textarea(
                attrs = {
                    'class' : 'textinput form-control',
                    'rows'  : '4'
                }
            )
        }


class FormSaidaProduto(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['produto'].queryset = Produto.objects.filter(is_deleted=False)
        self.fields['produto'].widget.attrs.update({'class': 'textinput form-control setprice stock', 'required': 'true'})
        self.fields['quantidade'].widget.attrs.update({'class': 'textinput form-control setprice quantity', 'min': '1', 'required': 'true'})
        self.fields['precounitario'].widget.attrs.update({'class': 'textinput form-control setprice price', 'min': '0', 'required': 'true'})
    class Meta:
        model = ProdutoSaida
        fields = ['produto', 'quantidade', 'precounitario']


FormSaidaProdutoPadrao = formset_factory(FormSaidaProduto, extra=1)




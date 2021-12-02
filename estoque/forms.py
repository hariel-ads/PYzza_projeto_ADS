from django import forms
from .models import Produto

class FormProduto(forms.ModelForm):
    def __init__(self, *args, **kwargs):                                                        
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['quantidade'].widget.attrs.update({'class': 'textinput form-control', 'min': '1'})

    class Meta:
        model = Produto
        fields = ['nome', 'quantidade']
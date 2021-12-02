from django.db import models
from estoque.models import Produto


class Fornecedor(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=12)
    endereco = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    cnpj = models.CharField(max_length=15)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
	    return self.nome


class RegistroEntrada(models.Model):
    registro = models.AutoField(primary_key=True)
    diahora = models.DateTimeField(auto_now=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete = models.CASCADE, related_name='purchasesupplier')

    def __str__(self):
	    return "Registro no: " + str(self.registro)

    def get_items_list(self):
        return ProdutoEntrada.objects.filter(registro=self)

    def get_total_price(self):
        produtosentrada = ProdutoEntrada.objects.filter(registro=self)
        total = 0
        for item in produtosentrada:
            total += item.precototal
        return total


class ProdutoEntrada(models.Model):
    registro = models.ForeignKey(RegistroEntrada, on_delete = models.CASCADE, related_name='purchasebillno')
    produto = models.ForeignKey(Produto, on_delete = models.CASCADE, related_name='purchaseitem')
    quantidade = models.IntegerField(default=1)
    precounitario = models.IntegerField(default=1)
    precototal = models.IntegerField(default=1)

    def __str__(self):
	    return "Registro no: " + str(self.registro.registro) + ", Item = " + self.produto.nome




class RegistroSaida(models.Model):
    registro = models.AutoField(primary_key=True)
    diahora = models.DateTimeField(auto_now=True)

    nome = models.CharField(max_length=150, default='exemplo')
    telefone = models.CharField(max_length=12, default=1234567899)
    endereco = models.CharField(max_length=200, default='teste')
    email = models.EmailField(max_length=254, default='email@email.com')
    cnpj = models.CharField(max_length=15, default=12345678912345)

    def __str__(self):
	    return "Registro no: " + str(self.registro)

    def get_items_list(self):
        return ProdutoSaida.objects.filter(registro=self)
        
    def get_total_price(self):
        produtossaida = ProdutoSaida.objects.filter(registro=self)
        total = 0
        for item in produtossaida:
            total += item.precototal
        return total


class ProdutoSaida(models.Model):
    registro = models.ForeignKey(RegistroSaida, on_delete = models.CASCADE, related_name='salebillno')
    produto = models.ForeignKey(Produto, on_delete = models.CASCADE, related_name='saleitem')
    quantidade = models.IntegerField(default=1)
    precounitario = models.IntegerField(default=1)
    precototal = models.IntegerField(default=1)

    def __str__(self):
	    return "Registro no: " + str(self.registro.registro) + ", Item = " + self.produto.nome


from django.db import models
    
class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    quantidade = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)

    @property
    def situacao_produto(self):
        if self.quantidade > 0 and self.quantidade <= 20:
            return "Situação/Ruim"
        elif self.quantidade > 20 and self.quantidade <= 40:
            return 'Situação/Regular'
        elif self.quantidade > 40 and self.quantidade <= 50:
            return 'Situação/Bom'
        elif self.quantidade > 50:
            return 'Situação/Excelente'

    def __str__(self):
	    return self.nome
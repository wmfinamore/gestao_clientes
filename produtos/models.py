from django.db import models


class Produto(models.Model):
    descricao = models.CharField(max_length=20)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.descricao
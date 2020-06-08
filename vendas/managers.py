from django.db import models
from django.db.models import Avg, Min, Max, Count


class VendaManager(models.Manager):
    def media(self):
        return self.all().aggregate(Avg('valor'))['valor__avg']

    def media_desc(self):
        return self.all().aggregate(Avg('desconto'))['desconto__avg']

    def min(self):
        return self.all().aggregate(Min('valor'))['valor__min']

    def max(self):
        return self.all().aggregate(Max('valor'))['valor__max']

    def qtd(self):
        return self.all().aggregate(Count('valor'))['valor__count']

    def qtd_fiscal(self):
        return self.filter(nfe_emitida=True
                           ).aggregate(Count('valor'))['valor__count']

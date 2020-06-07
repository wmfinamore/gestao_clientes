from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import Sum, F, FloatField, Max, Avg, Min, Count
from .models import Venda


class DashboardView(View):
    def get(self, request):
        media = Venda.objects.all().aggregate(Avg('valor'))['valor__avg']
        media_desc = Venda.objects.all().aggregate(Avg('desconto'))['desconto__avg']
        min = Venda.objects.all().aggregate(Min('valor'))['valor__min']
        max = Venda.objects.all().aggregate(Max('valor'))['valor__max']
        qtd = Venda.objects.all().aggregate(Count('valor'))['valor__count']
        qtd_fiscal = Venda.objects.filter(nfe_emitida=True).aggregate(Count('valor'))['valor__count']
        return render(request, 'vendas/dashboard.html', {'media': media,
                                                         'media_desc': media_desc,
                                                         'min': min,
                                                         'max': max,
                                                         'qtd': qtd,
                                                         'qtd_fiscal': qtd_fiscal,
                                                         })

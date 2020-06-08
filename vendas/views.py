from django.shortcuts import render
from django.views.generic.base import View
from .models import Venda


class DashboardView(View):
    def get(self, request):
        Venda.objects.media()
        media = Venda.objects.media()
        media_desc = Venda.objects.media_desc()
        min = Venda.objects.min()
        max = Venda.objects.max()
        qtd = Venda.objects.qtd()
        qtd_fiscal = Venda.objects.qtd_fiscal()
        return render(request, 'vendas/dashboard.html', {'media': media,
                                                         'media_desc': media_desc,
                                                         'min': min,
                                                         'max': max,
                                                         'qtd': qtd,
                                                         'qtd_fiscal': qtd_fiscal,
                                                         })

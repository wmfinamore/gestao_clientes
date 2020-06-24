from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Venda, ItemDoPedido
from .forms import ItemPedidoForm, ItemDoPedidoModelForm


class ListaVendas(View):
    def get(self, request):
        vendas = Venda.objects.all()
        return render(request, 'vendas/lista-vendas.html', {'vendas': vendas})


class EditPedido(View):
    def get(self, request, venda):
        data = {}
        venda = Venda.objects.get(id=venda)
        data['form_item'] = ItemPedidoForm()
        data['numero'] = venda.numero
        data['desconto'] = float(venda.desconto)
        data['venda'] = venda
        data['itens'] = venda.itemdopedido_set.all()

        return render(request, 'vendas/novo-pedido.html', data)


class DashboardView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('vendas.ver_dashboard'):
            return HttpResponse('Acesso Negado. Você precisa de permissão')

        return super(DashboardView, self).dispatch(request, *args, **kwargs)

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


class NovoPedido(View):
    def get(self, request):
        return render(request, 'vendas/novo-pedido.html')

    def post(self, request):
        data = {}
        data['form_item'] = ItemPedidoForm()
        data['numero'] = request.POST['numero']
        data['desconto'] = float(request.POST['desconto'].replace(',', '.'))
        data['venda_id'] = request.POST['venda_id']

        if data['venda_id']:
            venda = Venda.objects.get(id=data['venda_id'])
            venda.desconto = data['desconto']
            venda.numero = data['numero']
            venda.save()
        else:
            venda = Venda.objects.create(
                numero=data['numero'], desconto=data['desconto']
            )

        itens = venda.itemdopedido_set.all()
        data['venda'] = venda
        data['itens'] = itens
        return render(request, 'vendas/novo-pedido.html', data)


class NovoItemPedido(View):
    def get(self, request, pk):
        pass

    def post(self, request, venda):
        data = {}
        item = ItemDoPedido.objects.create(
            produto_id=request.POST['produto_id'],
            quantidade=request.POST['quantidade'],
            desconto=request.POST['desconto'],
            venda_id=venda
        )

        data['item'] = item
        data['form_item'] = ItemPedidoForm()
        data['numero'] = item.venda.numero
        data['desconto'] = item.venda.desconto
        data['venda'] = item.venda
        data['itens'] = item.venda.itemdopedido_set.all()

        return render(
            request, 'vendas/novo-pedido.html', data
        )


class DeletePedido(View):
    def get(self, request, venda):
        venda = Venda.objects.get(id=venda)
        return render(
            request, 'vendas/delete-pedido-confirm.html', {'venda': venda}
        )

    def post(self, request, venda):
        venda = Venda.objects.get(id=venda)
        venda.delete()
        return redirect('lista-vendas')


class DeleteItem(View):
    def get(self, request, item):
        item = ItemDoPedido.objects.get(id=item)
        return render(
            request, 'vendas/delete-item-confirm.html', {'item': item}
        )

    def post(self, request, item):
        item_pedido = ItemDoPedido.objects.get(id=item)
        venda_id = item_pedido.venda.id
        item_pedido.delete()
        return redirect('edit-pedido', venda=venda_id)

class EditItem(View):
    def get(self, request, item):
        item = ItemDoPedido.objects.get(id=item)
        form = ItemDoPedidoModelForm(instance=item)
        return render(
            request, 'vendas/edit-item.html', {'item': item, 'form': form}
        )

    def post(self, request, item):
        item_pedido = ItemDoPedido.objects.get(id=item)
        item_pedido.quantidade = request.POST['quantidade']
        item_pedido.desconto = request.POST['desconto']
        venda_id = item_pedido.venda.id
        item_pedido.save()
        return redirect('edit-pedido', venda=venda_id)

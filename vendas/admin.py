from django.contrib import admin
from .actions import nfe_nao_emitida, nfe_emitida
from .models import Venda, ItensDoPedido


class VendaAdmin(admin.ModelAdmin):
    readonly_fields = ('desconto',)
    list_filter = ('pessoa__doc', 'desconto')
    list_display = ('id', 'pessoa', 'nfe_emitida',)
    autocomplete_fields = ('pessoa',)
    search_fields = ('id', 'pessoa__first_name', 'pessoa__doc__num_doc')
    actions = [nfe_emitida, nfe_nao_emitida]


admin.site.register(Venda, VendaAdmin)
admin.site.register(ItensDoPedido)

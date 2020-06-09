from django.http import HttpResponseNotFound


def nfe_emitida(modelAdmin, request, queryset):
    if request.user.has_perm('vendas.setar_nfe'):
        queryset.update(nfe_emitida=True)
    else:
        return HttpResponseNotFound('<h1>Sem permissão</h1>')

nfe_emitida.short_description = "NF-e emitida"


def nfe_nao_emitida(modelAdmin, request, queryset):
    queryset.update(nfe_emitida=False)

nfe_nao_emitida.short_description = "NF-e não emitida"
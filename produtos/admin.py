from django.contrib import admin
from .models import Produto


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'preco')
    search_fields = ('descricao',)


admin.site.register(Produto, ProdutoAdmin)
from django.contrib import admin
from .models import Person, Documento, Venda, Produto


class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            'Dados Pessoais', {'fields': ('first_name', 'last_name', 'doc')}
        ),
        (
            'Dados Complementares', {
                'classes': ('collapse', ),
                'fields': ('age', 'salary', 'photo', 'bio')}
        )
    )
    # fields = (('doc', 'first_name'), 'last_name', ('age', 'salary'), 'bio', 'photo')
    # exclude = ('bio', )
    list_filter = ('age', 'salary')
    list_display = ('first_name', 'doc', 'last_name', 'age', 'salary', 'bio', 'tem_foto')

    def tem_foto(self, obj):
        if obj.photo:
            return 'Sim'
        else:
            return 'Não'

    tem_foto.short_description = 'Possui foto'


class VendaAdmin(admin.ModelAdmin):
    readonly_fields = ('desconto',)
    list_filter = ('pessoa__doc', 'desconto')
    """raw_id_fields traz um campo de busca, ao invés de um drop down"""
    raw_id_fields = ('pessoa',)
    search_fields = ('id', 'pessoa__first_name', 'pessoa__doc__num_doc')


admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Produto)

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
    list_display = ('first_name', 'doc', 'last_name', 'age', 'salary', 'bio', 'photo')
    list_filter = ('age', 'salary')

class VendaAdmin(admin.ModelAdmin):
    list_filter = ('pessoa__doc', 'desconto')


admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Produto)

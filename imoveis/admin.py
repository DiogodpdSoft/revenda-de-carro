from django.contrib import admin
from .models import Imovel, ImagemImovel

class ImagemImovelInline(admin.TabularInline):
    model = ImagemImovel
    extra = 1

@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tipo', 'finalidade', 'cidade', 'preco', 'quartos', 'ano_fabricacao', 'destaque']
    list_filter = ['tipo', 'finalidade', 'cidade', 'destaque']
    search_fields = ['titulo', 'endereco', 'bairro', 'cidade']
    prepopulated_fields = {'slug': ('titulo',)}
    list_editable = ['destaque']
    inlines = [ImagemImovelInline]
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('titulo', 'tipo', 'finalidade', 'preco', 'destaque', 'slug')
        }),
        ('Localização', {
            'fields': ('endereco', 'bairro', 'cidade')
        }),
        ('Características', {
            'fields': ('metragem', 'quartos', 'banheiros', 'vagas', 'ano_fabricacao')
        }),
        ('Descrição', {
            'fields': ('descricao',)
        }),
    )

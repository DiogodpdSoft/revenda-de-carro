from django.contrib import admin
from .models import MensagemContato

@admin.register(MensagemContato)
class MensagemContatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'telefone', 'data']
    list_filter = ['data']
    search_fields = ['nome', 'email', 'telefone', 'mensagem']
    readonly_fields = ['nome', 'email', 'telefone', 'mensagem', 'data']
    
    def has_add_permission(self, request):
        return False  # Impede a criação manual de mensagens no admin
    
    def has_change_permission(self, request, obj=None):
        return False  # Impede a edição de mensagens no admin

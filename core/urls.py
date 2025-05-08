from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('imoveis.urls')),
    path('contato/', include('contato.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Configurando o admin
admin.site.site_header = 'Deise Santos Imóveis'
admin.site.site_title = 'Administração Deise Santos Imóveis'
admin.site.index_title = 'Administração do Site'

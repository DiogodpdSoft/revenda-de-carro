from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contato/', include('contato.urls')),
    path('', include('carros.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Configurando o admin
admin.site.site_header = 'Revenda de Carros'
admin.site.site_title = 'Administração Revenda de Carros'
admin.site.index_title = 'Administração do Site'

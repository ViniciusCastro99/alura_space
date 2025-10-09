from django.contrib import admin
from django.urls import path, include ##include serve para importar as url's do app galeria que foram isoladas o arquivo url's.py dentro da aplicação

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')) #utilizando o include para importar as rotas isoladas.
]

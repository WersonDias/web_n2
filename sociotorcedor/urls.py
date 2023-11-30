# sociotorcedor/urls.py
from django.urls import path
from .views import lista_socios, cadastrar_socio, editar_socio, excluir_socio

urlpatterns = [
    path('', lista_socios, name='lista_socios'),
    path('cadastrar/', cadastrar_socio, name='cadastrar_socio'),
    path('editar/<int:pk>/', editar_socio, name='editar_socio'),
    path('excluir/<int:pk>/', excluir_socio, name='excluir_socio'),
]

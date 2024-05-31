from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_historias, name='listar_historias'),
    path('historia_clinica/<int:id>/', views.detalle_historia, name='detalle_historia_clinica'),
    path('descargar_historia_clinica/<int:id>/', views.descargar_historia_clinica, name='descargar_historia_clinica'),
]


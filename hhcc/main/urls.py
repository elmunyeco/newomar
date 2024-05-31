from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_historias, name='listar_historias'),
    path('historia_clinica/<int:id>/', views.detalle_historia, name='detalle_historia'),
    path('descargar_historia_clinica/<int:id>/', views.descargar_historia_clinica, name='descargar_historia_clinica'),
       path('nuevo_signo_vital/', views.nuevo_signo_vital, name='nuevo_signo_vital'),
    path('editar_diagnostico/', views.editar_diagnostico, name='editar_diagnostico'),
    path('listar_indicaciones/<int:id>/', views.listar_indicaciones, name='listar_indicaciones'),
    path('listar_solicitudes/<int:id>/', views.listar_solicitudes, name='listar_solicitudes'),
]

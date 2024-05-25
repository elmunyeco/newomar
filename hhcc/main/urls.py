from django.urls import path, include
from . import views

urlpatterns = [
    path('historias/', views.listar_historias, name='listar_historias'),
    path('historia/<int:id>/', views.detalle_historia, name='detalle_historia'),
]

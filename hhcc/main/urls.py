from django.urls import path
from . import views

urlpatterns = [
    path('historias/', views.listar_historias, name='listar_historias'),
    path('historia/<int:id>/', views.detalle_historia, name='detalle_historia'),
]


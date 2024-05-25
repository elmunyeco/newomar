from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import HistoriaClinica

def listar_historias(request):
    query = request.GET.get('campoBuscador', '')
    filtro = request.GET.get('tipoFiltro', '4')
    if filtro == '4':
        historias = HistoriaClinica.objects.filter(documento__icontains(query))
    elif filtro == '3':
        historias = HistoriaClinica.objects.filter(apellido__icontains(query))
    elif filtro == '2':
        historias = HistoriaClinica.objects.filter(nombre__icontains(query))
    elif filtro == '1':
        historias = HistoriaClinica.objects.filter(numero__icontains(query))
    else:
        historias = HistoriaClinica.objects.all()

    paginator = Paginator(historias, 10)  # 10 historias por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': query,
        'tipoFiltro': filtro
    }

    return render(request, 'main/listar_historias.html', context)

def detalle_historia(request, id):
    historia = get_object_or_404(HistoriaClinica, id=id)
    return render(request, 'main/detalle_historia.html', {'historia': historia})


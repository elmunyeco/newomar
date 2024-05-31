from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import HistoriaClinica

def listar_historias(request):
    query = request.GET.get('campoBuscador', '')
    filtro = request.GET.get('tipoFiltro', '4')
    if filtro == '4':
        historias = HistoriaClinica.objects.filter(documento__icontains=query)
    elif filtro == '3':
        historias = HistoriaClinica.objects.filter(apellido__icontains=query)
    elif filtro == '2':
        historias = HistoriaClinica.objects.filter(nombre__icontains=query)
    elif filtro == '1':
        historias = HistoriaClinica.objects.filter(numero__icontains=query)
    else:
        historias = HistoriaClinica.objects.all()

    paginator = Paginator(historias, 14)  # 10 historias por página
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


from .models import HistoriaClinica, Enfermedad, SignosVitales

def detalle_historia(request, id):
    historia_clinica = get_object_or_404(HistoriaClinica, pk=id)
    enfermedades = Enfermedad.objects.all()
    signos_vitales = SignosVitales.objects.filter(historia_clinica=historia_clinica).last()
    estudios = [
        {"nombre": "Ecocardiograma", "url": "https://estudioadb.com/index.php/eco/nuevoEstudio/{}".format(id)},
        {"nombre": "Carotidas", "url": "https://estudioadb.com/index.php/carotidas/nuevoEstudio/{}".format(id)},
        {"nombre": "Doppler", "url": "https://estudioadb.com/index.php/doppler/nuevoEstudio/{}".format(id)},
        {"nombre": "Ecostress", "url": "https://estudioadb.com/index.php/stress/nuevoEstudio/{}".format(id)},
    ]
    context = {
        'historia_clinica': historia_clinica,
        'enfermedades': enfermedades,
        'signos_vitales': signos_vitales,
        'estudios': estudios,
    }
    return render(request, 'main/detalle_historia.html', context)

def descargar_historia_clinica(request, id):
    historia_clinica = get_object_or_404(HistoriaClinica, pk=id)
    # Aquí debes implementar la lógica para generar el archivo a descargar
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="historia_clinica_{historia_clinica.id}.pdf"'
    # Aquí deberías agregar el contenido del archivo PDF
    response.write("Contenido del PDF de la historia clínica")
    return response

def descargar_historia_clinica(request, id):
    historia_clinica = get_object_or_404(HistoriaClinica, pk=id)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="historia_clinica_{historia_clinica.id}.pdf"'
    response.write("Contenido del PDF de la historia clínica")
    return response

def nuevo_signo_vital(request):
    # Lógica para guardar nuevo signo vital
    pass

def editar_diagnostico(request):
    # Lógica para editar diagnóstico
    pass

def listar_indicaciones(request, id):
    # Lógica para listar indicaciones
    pass

def listar_solicitudes(request, id):
    # Lógica para listar solicitudes
    pass


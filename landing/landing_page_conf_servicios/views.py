from django.shortcuts import render

def landing_page(request):
    context = {
        'titulo_principal': "Análisis y Gestión de la Continuidad del Negocio y Clústeres",
        'subtitulo': "Informe Detallado sobre Arquitecturas de Clústeres, Riesgo y Recuperación de Desastres (RPO/RTO)",
    }
    return render(request, 'landing_page_conf_servicios/landing_page.html', context)

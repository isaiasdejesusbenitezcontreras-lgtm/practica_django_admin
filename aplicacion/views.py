from django.shortcuts import render
from .models import Noticia

def portal_noticias(request):
    noticias = Noticia.objects.all().order_by('-fecha')
    return render(request, 'aplicacion/portal.html', {'noticias': noticias})



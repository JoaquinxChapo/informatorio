from django.shortcuts import render
from django.http.response import Http404
from .models import Tarjetas, Trabajos,InfoIndex, Noticias, Team
from django.http import HttpResponse



def index(request):
    ultimotarjeta= Tarjetas.objects.all().order_by('creado').reverse()[:3]
    ultimotrabajo=Trabajos.objects.all().order_by('creado').reverse()[:3]
    ultimoinfo=InfoIndex.objects.all().order_by('creado').reverse()[:3]
    ultimanoticia=Noticias.objects.all().order_by('creado').reverse()[:3]
    ultimoteam=Team.objects.all()
    context ={ 
        'tarjetasdestacadas':ultimotarjeta,
        'MEDIA_ROOT':'media/img/mages',
        'trabajodestacada':ultimotrabajo,
        'indexdestacado':ultimoinfo,
        'noticadestacada':ultimanoticia,
        'teamdeastacado': ultimoteam

    }
    return render (request,'index.html', context)
def login(request):
    return render(request,'login.html',{})
def registro(request):
    return render(request,'registro.html',{} )
def noticia(request):
    return render(request,'noticias.html',{})
# Create your views here.

from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
from galeria.models import Fotografia

# Create your views here.

def index(request):
    
    '''dados = {
        1: {"nome" : "Nebulosa de Carina",
            "legenda" : "webbtelecope.org  /NASA / James Webb"},
        2: {"nome" : "Galáxia NGC 1079",
            "legenda" : "nasa.org / NASA / Hubble"}
    }'''
    #fotografias = Fotografia.objects.all()
    # fotografias = Fotografia.objects.filter(publicada=True) # order_by("-data_fotografia") decrescente
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    
    # return HttpResponse('<h1>Alura Space</h1>')
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    
    fotografia = get_object_or_404(Fotografia, pk=foto_id)

    return render(request, 'galeria/imagem.html', {"fotografia" : fotografia})


def buscar(request):
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    
    if 'buscar' in request.GET:
        nome_a_ser_pesquisado = request.GET['buscar']
        
        if nome_a_ser_pesquisado:
            fotografias = fotografias.filter(nome__icontains=nome_a_ser_pesquisado)
    
    return render(request, 'galeria/buscar.html', {"cards" : fotografias})




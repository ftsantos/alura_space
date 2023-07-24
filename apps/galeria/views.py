from django.shortcuts import render, get_object_or_404, redirect
#from django.http import HttpResponse
from django.contrib import messages

from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms

# Create your views here.

def index(request):
    
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário precisa estar logado')
        return redirect('login')
    
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
    
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário precisa estar logado')
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    
    if 'buscar' in request.GET:
        nome_a_ser_pesquisado = request.GET['buscar']
        
        if nome_a_ser_pesquisado:
            fotografias = fotografias.filter(nome__icontains=nome_a_ser_pesquisado)
    
    return render(request, 'galeria/index.html', {"cards" : fotografias})

def nova_imagem(request):
    
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário precisa estar logado')
        return redirect('login')
    
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova fotografia cadastrada')
    
    form = FotografiaForms
    return render(request, 'galeria/nova_imagem.html', {'form': form})

def editar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)
    
    if request.method == 'POST':
         form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
         
         if form.is_valid():
            form.save()
            messages.success(request, 'Fotografia editada com sucesso')
            return redirect('index')
    
        
    return render(request, 'galeria/editar_imagem.html', {'form': form, 'foto_id': foto_id})
    
def deletar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Deleção feita com sucesso')
    return redirect('index')
    
def filtro(request, categoria):
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True, categoria=categoria)
    return render(request, 'galeria/index.html', {"cards": fotografias})

from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from django.utils import timezone

#from .models import Questao, Opcao

def areacomum(request):
    return render(request, 'areas/areacomum.html')

def apostar(request):
    return render(request, 'areas/apostar.html')

def areapessoal(request):
    return render(request, 'areas/areapessoal.html')

def mostrardados(request):
    return render(request, 'areas/mostrardados.html')

def editardados(request):
    return render(request, 'areas/editardados.html')

def carregarsaldo(request):
    return render(request, 'areas/carregarsaldo.html')


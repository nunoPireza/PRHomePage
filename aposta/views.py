from django.shortcuts import render, get_object_or_404
from .models import Concurso, Aposta, Conta
from django.template import loader

def aposta(request):
    apostas_list = Aposta.objects.all()
    template = loader.get_template('aposta/index.html')
    context = {'apostas_list': apostas_list}
    return render(request, 'aposta/index.html', context)

def detalhe(request, aposta_id):
    aposta = get_object_or_404(Aposta, pk=aposta_id)
    return render(request, 'aposta/detalhe.html', {'aposta': aposta})

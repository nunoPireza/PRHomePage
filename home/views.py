from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse


def homepage(request):
    return render(request, 'home/homepage.html')

def returnHomepage(request):
    return HttpResponseRedirect(reverse('home/homepage.html'))


def novaconta(request):
    return render(request, 'home/novaconta.html')


def areacomum(request):
    return render(request, 'home/areacomum.html')

def admin(request):
    return render(request, 'home/admin.html')

def recuperarPass(request):
    return render(request, 'home/recuperarPass.html')

def fazerAposta(request):
    return render(request, 'home/aposta.html')

def gravaAposta(request):
    texto=request.POST['aposta']
    q=Questao(questao_texto=texto, pub_data= timezone.now())
    q.save()
    return HttpResponseRedirect(reverse('votacao:index'))
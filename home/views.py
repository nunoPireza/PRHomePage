from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings
from  django.core.mail import send_mail

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

def criarUtilizador(request):
    titulo = 'Email de confirmação  de registo'
    mensagem = 'Bem vindo ao site de apostas..bla bla bla'
    emaildestino = 'nmfpa@iscte.pt'
    send_mail(titulo,mensagem,settings.EMAIL_HOST_USER,emaildestino,fail_silently=True)


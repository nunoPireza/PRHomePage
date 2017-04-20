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

def mandaEmail(request):
    emaildestino = request.POST['email']
    titulo = 'Email de confirmação  de registo'
    mensagem = 'Bem vindo ao site de apostas..bla bla bla'
    send_mail(titulo, mensagem, settings.EMAIL_HOST_USER, emaildestino, fail_silently=True)

def registo(request):
    return render(request, 'home/registo.html')

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import Utilizador
from django.contrib.auth import authenticate, login

def inicio(request):
    return render(request, 'home/inicio.html')

def exitMenor(request):
    return render(request, 'home/exitMenor.html')

def homepage(request):
    return render(request, 'home/homepage.html')

def returnHomepage(request):
    return HttpResponseRedirect(reverse('home/homepage.html'))

def areacomum(request):
    return render(request, 'home/areacomum.html')

def admin(request):
    return render(request, 'home/admin.html')

def recuperarPass(request):
    return render(request, 'home/recuperarPass.html')

def fazerAposta(request):
    return render(request, 'home/aposta.html')

def novoRegisto(request):
    if request.POST['input_username'] is '':
        context = {'invalid_user': True}
        return render(request, "home/registo.html", context)

    if request.POST['input_email'] is '':
        context = {'invalid_email': True}
        return render(request, "home/registo.html", context)

    if request.POST['input_password'] is '':
        context = {'invalid_pass': True}
        return render(request, "home/registo.html", context)

    if request.POST['input_name'] is '':
        context = {'invalid_name': True}
        return render(request, "home/registo.html", context)

    if request.POST['input_surname'] is '':
        context = {'invalid_last': True}
        return render(request, 'home/registo.html', context)
    else:
        try:
            fuser = User.objects.create_user(request.POST['input_username'], request.POST['input_email'],
                                             request.POST['input_password'])
            fuser.first_name = request.POST['input_name']
            fuser.last_name = request.POST['input_surname']
            fuser.save()
        except:
            context = {}
            context['same_user'] = True
            return render(request, 'home/registo.html', context)

        fuser = Utilizador(user=fuser)
        if request.POST['input_nif']:
            fuser.NIF = request.POST['input_nif']
        if request.POST['input_morada']:
            fuser.morada = request.POST['input_morada']
        if request.POST['input_codpostal']:
            fuser.codigopostal = request.POST['input_codpostal']
        if request.POST['input_contacto']:
            fuser.contacto = request.POST['input_contacto']
        if request.POST['input_loc']:
            fuser.localidade = request.POST['input_loc']
        if request.POST['input_pais']:
            fuser.pais = request.POST['input_pais']

        fuser.save()

        emaildestino = request.POST['input_email']
        destinatario = request.POST['input_name'] + " " + request.POST['input_surname']
        titulo = 'Email de confirmação de registo'
        mensagem = 'Bem vindo ao site de apostas ' + destinatario + "."
        send_mail(titulo, mensagem, settings.EMAIL_HOST_USER, [emaildestino], fail_silently=False)
        return render(request, 'home/homepage.html')


def registo(request):
    return render(request, 'home/registo.html')

def loginpage(request):
    return render(request, 'home/loginpage.html')

def loginview(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username = username, password = password)
    if user is not None:
        login(request, user)
        return render(request, 'home/homepage.html')
    else:
        return HttpResponse('Falhou')


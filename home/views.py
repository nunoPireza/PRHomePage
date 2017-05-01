from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect, redirect
from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError
from .models import Utilizador
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm

def inicio(request):
    return render(request, 'home/inicio.html')

def exitMenor(request):
    return render(request, 'home/exitMenor.html')

def homepage(request):
    return render(request, 'home/homepage.html')

<<<<<<< HEAD
def returnHomepage(request):
    return HttpResponseRedirect(reverse('home/homepage.html'))

def personalpage(request):
    args = {}
    for each in User._meta.fields:
        args[each.name] = getattr(User, each.name)
    return render(request, 'home/personalpage.html', args)

def areacomum(request):
    return render(request, 'home/areacomum.html')

=======
>>>>>>> origin/master
def admin(request):
    return render(request, 'home/admin.html')


<<<<<<< HEAD
def fazerAposta(request):
    return render(request, 'home/aposta.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'home/homepage.html')
    else:
        form = UserCreationForm()

    args = {'form':form}
    return render(request, 'home/reg_form.html', args)

=======
>>>>>>> origin/master
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
        send_mail(titulo, mensagem, settings.EMAIL_HOST_USER, [emaildestino], fail_silently=True)
        return render(request, 'home/homepage.html')


def registo(request):
    return render(request, 'home/registo.html')

def loginpage(request):
    return render(request, 'home/loginpage.html')

def loginview(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    context = {}
    if user is not None:
        login(request, user)
        args = {}
        for each in User._meta.fields:
            args[each.name] = getattr(User, each.name)
        return render(request, 'home/personalpage.html', args)

    else:
        context['noUser'] = True
        return render(request, "home/loginpage.html", context)

def logoutview(request):
    logout(request)
    return render(request, 'home/logout.html')


def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST, user=request.user)

        if form.is_valid():
            form.save()
            return redirect('/siteapostas/personalpage')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'home/changepassword.html')

def submeterpass(request):
    acco = get_object_or_404(Utilizador, user=request.user)
    context = {}
    context['acc'] = acco
    if request.user.is_authenticated:
        try:
            if request.user.check_password(request.POST['oldpassword']):
                if request.POST['newpassword'] == request.POST['confnewpassword']:
                    request.user.set_password(request.POST['newpassword'])
                    request.user.save()

                    return render(request, "home/personalpage.html")
                else:
                    context['no_match'] = True
                    return render(request, "home/changepassword.html", context)
            else:
                context['old'] = True
                return render(request, "home/changepassword.html", context)

        except MultiValueDictKeyError:
            return HttpResponseRedirect(reverse('home:changepassword'))
    else:
        return HttpResponse("É necessário estar autenticado.")
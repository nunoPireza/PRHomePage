from django.shortcuts import render


def aposta(request):
    return render(request, 'aposta/aposta.html')

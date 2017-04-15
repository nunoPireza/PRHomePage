from django.shortcuts import render

# Create your views here.
def apostas(request):
    return render(request,'aposta/apostas.html')
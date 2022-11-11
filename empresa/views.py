from django.shortcuts import render


def novaempresa(request):
    return render(request, 'empresa/novaempresa.html')

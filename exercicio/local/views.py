from django.shortcuts import render

def local(request):
    return render(request, 'local/index.html')

def localizacao(request):
    return render(request, 'local/localizacao.html')


from django.shortcuts import render

def outros(request):
    return render(request, 'outros/index.html')

def atividade(request):
    return render(request, 'atividade/atividade.html')


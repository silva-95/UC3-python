from django.shortcuts import render

# Create your views here.
contexto = {
    'title': 'Unidades - Salão de Beleza Visual da Moda'
}


def unidade(request):
   
    return render(
                request, 
                "unidade/index.html",
                contexto
                
                )
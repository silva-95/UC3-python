from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def contato(request):
    print("Passei pelo contato")
    return HttpResponse("<body bgcolor='#fff8dc'><h1>Contato</h1><p>Renan Silva</p><p>Email: 9B2Np@example.com</p></body>")
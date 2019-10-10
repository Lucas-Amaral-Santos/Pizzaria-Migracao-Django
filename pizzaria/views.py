from django.shortcuts import get_object_or_404
#from django.http import HttpResponse
from .models import Categoria, Produto

# from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Olá Mundo! Você está vendo o conteúdo da view index da aplicação 'produto'")
    frase = "Olá mundo";
    return render(request, 'pizzaria/index.html', {'frase': frase})

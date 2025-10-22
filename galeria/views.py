from django.shortcuts import render




def index(request):
    ##Cria um dicionario de dicionários com informações da imagens, essas informações serão exíbidas nos cards
    dados = {
    1: {
        "nome": "Nebulosa de Carina",
        "legenda": "webbtelescope.org / NASA / James Webb"
        },
    2: {
        "nome": "Galáxia NGC 1079",
        "legenda": "nasa.org / NASA / Hubble"
       }
    }

    return render(request, 'galeria/index.html', {"cards": dados}) ##Passa o dicionários de dados das imagens, criado anteriormente.

def imagem(request):
    return render(request, 'galeria/imagem.html')
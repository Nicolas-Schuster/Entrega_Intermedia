from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
    context = {
        'raiz':'Bienvenidos al INICIO, disfrute su compra ',
        'text': 'Estamos trabajando para ofrecerle un buen servicio',
        'text2':'En un futuro podra gozar mejor de este proyecto prototipo 1 saludos ',
    }
    return render(request, 'inicio.html', context=context)



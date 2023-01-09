from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
    context = {
        'raiz':'Bienvenidos al INICIO, disfrute su compra ',

    }
    return render(request, 'inicio.html', context=context)
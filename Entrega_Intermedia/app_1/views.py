from django.shortcuts import render
from django.http import HttpResponse
from app_1.models import Electrodomesticos, Tecnologia, Hogar, Herramientas, Indumentaria, Perfumeria, Automotor

def saludo(request):
    return HttpResponse('Hola estamos comprobando')

def new_product(request):
    if request.method == 'GET':
        return render(request, 'create.html/', context = {} )

    elif request.method == 'POST':
        Electrodomesticos.objects.create(name = request.POST['name'], price = request.POST['price'], shipping_cost = request.POST['shipping_cost'], description = request.POST['description'])
        return render(request, 'create.html/', context={})
        

def electro(request):
    all_electrodomesticos = Electrodomesticos.objects.all()
    context = {
        'stock electro':all_electrodomesticos,
    }
    return render(request, 'electrodomesticos.html/', context=context)

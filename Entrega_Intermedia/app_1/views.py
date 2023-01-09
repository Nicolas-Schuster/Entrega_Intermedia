from django.shortcuts import render
from django.http import HttpResponse
from app_1.models import Electrodomesticos, Tecnologia, Hogar, Herramientas, Indumentaria, Perfumeria, Automotor
from app_1.forms import ElectrodomesticosForm, TecnologiaForm, HogarForm, HerramientasForm, IndumentariaForm, PerfumeriaForm, AutomotorForm



def saludo(request):
    return HttpResponse('Hola estamos comprobando')

def new_product(request):
    if request.method == 'GET':
        context ={
            'form': ElectrodomesticosForm()
        }
        return render(request, 'create.html/', context = context)

    elif request.method == 'POST':
        Electrodomesticos.objects.create(name = request.POST['name'], price = request.POST['price'], shipping_cost = request.POST['shipping_cost'], description = request.POST['description'])
        return render(request, 'create.html/', context={})
        

def electro(request):
    all_electrodomesticos = Electrodomesticos.objects.all()
    context = {
        'stock_electro':all_electrodomesticos,
    }
    return render(request, 'electrodomesticos.html/', context=context)


def new_pc(request):
    if request.method == 'GET':
        context = {
            'form': TecnologiaForm()
        }
        return render(request, 'create1.html/', context = context)

    elif request.method == 'POST':
        form = TecnologiaForm(request.POST)
        if form.is_valid():
            Tecnologia.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],
                shipping_cost = form.cleaned_data['shipping_cost'],
                stock = form.cleaned_data['stock'],
                )
            context = {
                'message': 'Producto creado'
            }
            return render(request, 'create1.html/', context=context)
        else:
            context ={
                'forms_errors': form.errors,
                'form':TecnologiaForm()
            }
        return render(request, 'create1.html/', context=context)


def tecno(request):
    if 'search' in request.GET:
        search = request.GET['search']
        all_tecnos = Tecnologia.objects.filter(name__contains=search)
    else:
        all_tecnos = Tecnologia.objects.all()
    context = {
        'stock_tecno':all_tecnos,
    }
    return render(request, 'tecnologia.html/', context=context)
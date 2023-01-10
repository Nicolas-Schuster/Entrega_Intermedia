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
        form = ElectrodomesticosForm(request.POST)
        if form.is_valid():
            Electrodomesticos.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],
                shipping_cost = form.cleaned_data['shipping_cost'],
                stock = form.cleaned_data['stock'],
                )
            context = {
                'message': 'Producto creado'
            }
            return render(request, 'create.html/', context=context)
        else:
            context ={
                'forms_errors': form.errors,
                'form':ElectrodomesticosForm()
            }
        return render(request, 'create1.html/', context=context)
        

def electro(request):
    if 'search' in request.GET:
        search = request.GET['search']
        all_electrodomesticos = Electrodomesticos.objects.filter(name__contains=search)
    else:
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


def new_house(request):
    if request.method == 'GET':
        context = {
            'form': HogarForm()
        }
        return render(request, 'create2.html/', context = context)

    elif request.method == 'POST':
        form = HogarForm(request.POST)
        if form.is_valid():
            Hogar.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],
                shipping_cost = form.cleaned_data['shipping_cost'],
                stock = form.cleaned_data['stock'],
                )
            context = {
                'message': 'Producto creado'
            }
            return render(request, 'create2.html/', context=context)
        else:
            context ={
                'forms_errors': form.errors,
                'form':HogarForm()
            }
        return render(request, 'create2.html/', context=context)


def house(request):
    all_houses = Hogar.objects.all()
    context = {
        'stock_house':all_houses,
    }
    return render(request, 'hogar.html/', context=context)


def new_tool(request):
    if request.method == 'GET':
        context = {
            'form': HerramientasForm()
        }
        return render(request, 'create3.html/', context = context)

    elif request.method == 'POST':
        form = HerramientasForm(request.POST)
        if form.is_valid():
            Herramientas.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],
                shipping_cost = form.cleaned_data['shipping_cost'],
                stock = form.cleaned_data['stock'],
                )
            context = {
                'message': 'Producto creado'
            }
            return render(request, 'create3.html/', context=context)
        else:
            context ={
                'forms_errors': form.errors,
                'form':HerramientasForm()
            }
        return render(request, 'create3.html/', context=context)


def tools(request):
    all_tools = Herramientas.objects.all()
    context = {
        'stock_tools':all_tools,
    }
    return render(request, 'herramientas.html/', context=context)


def new_garment(request):
    if request.method == 'GET':
        context = {
            'form': IndumentariaForm()
        }
        return render(request, 'create4.html/', context = context)

    elif request.method == 'POST':
        form = IndumentariaForm(request.POST)
        if form.is_valid():
            Indumentaria.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],
                shipping_cost = form.cleaned_data['shipping_cost'],
                stock = form.cleaned_data['stock'],
                )
            context = {
                'message': 'Producto creado'
            }
            return render(request, 'create4.html/', context=context)
        else:
            context ={
                'forms_errors': form.errors,
                'form':IndumentariaForm()
            }
        return render(request, 'create4.html/', context=context)


def garments(request):
    all_garments = Indumentaria.objects.all()
    context = {
        'stock_garments':all_garments,
    }
    return render(request, 'indumentaria.html/', context=context)


def new_fragance(request):
    if request.method == 'GET':
        context = {
            'form': PerfumeriaForm()
        }
        return render(request, 'create5.html/', context = context)

    elif request.method == 'POST':
        form = PerfumeriaForm(request.POST)
        if form.is_valid():
            Perfumeria.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],
                shipping_cost = form.cleaned_data['shipping_cost'],
                stock = form.cleaned_data['stock'],
                )
            context = {
                'message': 'Producto creado'
            }
            return render(request, 'create5.html/', context=context)
        else:
            context ={
                'forms_errors': form.errors,
                'form':PerfumeriaForm()
            }
        return render(request, 'create5.html/', context=context)


def fragance(request):
    all_fragances = Perfumeria.objects.all()
    context = {
        'stock_fragances':all_fragances,
    }
    return render(request, 'perfumeria.html/', context=context)


def new_accesories(request):
    if request.method == 'GET':
        context = {
            'form': AutomotorForm()
        }
        return render(request, 'create6.html/', context = context)

    elif request.method == 'POST':
        form = AutomotorForm(request.POST)
        if form.is_valid():
            Automotor.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],
                shipping_cost = form.cleaned_data['shipping_cost'],
                stock = form.cleaned_data['stock'],
                )
            context = {
                'message': 'Producto creado'
            }
            return render(request, 'create6.html/', context=context)
        else:
            context ={
                'forms_errors': form.errors,
                'form':AutomotorForm()
            }
        return render(request, 'create6.html/', context=context)


def accesories(request):
    all_accesories = Automotor.objects.all()
    context = {
        'stock_accesories':all_accesories,
    }
    return render(request, 'automotor.html/', context=context)





















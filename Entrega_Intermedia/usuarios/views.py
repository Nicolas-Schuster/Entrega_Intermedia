from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView
from usuarios.forms import RegistroForm


class Registro_De_Usuario(CreateView):
    model = User
    template_name = 'registrar.html'
    form_class =RegistroForm
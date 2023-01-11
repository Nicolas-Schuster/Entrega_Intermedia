from django.urls import path
from usuarios.views import Registro_De_Usuario



urlpatterns = [
    path('registrar/', Registro_De_Usuario.as_view(), name = 'registrar')
]
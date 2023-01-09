from django.urls import path

from app_1.views import new_product, saludo, electro

urlpatterns = [
    path('create/', new_product),
    path('saludo/', saludo),
    path('electro/', electro )



    
]
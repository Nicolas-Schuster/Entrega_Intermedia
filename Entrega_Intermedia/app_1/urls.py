from django.urls import path

from app_1.views import new_product, saludo, electro, new_pc, tecno

urlpatterns = [
    path('create/', new_product),
    path('saludo/', saludo),
    path('electro/', electro ),
    path('tecnologia/', tecno),
    path('create1/', new_pc)

    
]
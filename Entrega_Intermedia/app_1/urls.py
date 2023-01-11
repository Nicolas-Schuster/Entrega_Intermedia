from django.urls import path

from app_1.views import new_product, electro, new_pc, tecno, house, new_house, tools, new_tool, garments, new_garment, fragance, new_fragance, accesories, new_accesories, all

urlpatterns = [
    path('create/', new_product),
    path('electro/', electro ),
    path('tecnologia/', tecno),
    path('create1/', new_pc),
    path('hogar/', house),
    path('create2/', new_house),
    path('herramientas/', tools),
    path('create3/', new_tool),
    path('indumentaria/', garments),
    path('create4/', new_garment),
    path('perfumeria/', fragance),
    path('create5/', new_fragance),
    path('automotor/', accesories),
    path('create6/', new_accesories),
    path('all/', all),

    
]
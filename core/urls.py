from django.urls import path
from core.views import *

urlpatterns = [
    path('product/', Renderizer.index_product_template ),
    path('product/create/', ProductView.create,  name="product-create"),
    path("product/index/", ProductView.index, name="product-index"),
    path("product/show/<int:id>", ProductView.show, name="product-show"),
    path("product/show/update/<int:id>", ProductView.show_update, name="product-show-update"),
    path("product/update/<int:id>", ProductView.update, name="product-update"),
    path("product/delete/<int:id>", ProductView.delete, name="product-delete"),
    
    #Renderizar Template
    
    path("d'neiser/plantilla", Renderizer.index_plantilla),
    path("d'neiser/diplomado", Renderizer.index_pagina_diplomado),
    path("d'neiser/maqui", Renderizer.index_maqui_page, name="maqui"),
    path("d'neiser/golosina", Renderizer.index_golosina_page),
]
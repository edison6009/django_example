from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from core.models import *

# Create your views here.   
class ProductView(View):
    def create(request):
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description", "")
        available = request.POST.get("available") == "on"
        category_id = request.POST.get("category")
        category = Category.objects.filter(id=category_id).first() if category_id else None

        new_product = Product.objects.create(
            name=name,
            price=price,
            description=description,
            available=available,
            category=category
        )

        return HttpResponse(f"<h1> !!Producto creado exitosamente!! </h1> <br> {new_product}")

    def index(request):
        products = Product.objects.all()
        return render(request, "product.html", {"products": products})
    
    def show(request,id):
        product = Product.objects.get(id=id)
        return render(request, "product_show.html", {"product": product})
    
    def show_update(request,id):
        product = Product.objects.get(id=id)
        return render(request, "product_update.html", {"product": product})
    
    def update(request, id):
        product = Product.objects.filter(id=id).first()
        if not product:
            return HttpResponse("<h1>Producto no encontrado</h1>")

        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description", "")
        available = request.POST.get("available") == "on"
        category_id = request.POST.get("category")
        category = Category.objects.filter(id=category_id).first() if category_id else None

        product.name = name
        product.price = price
        product.description = description
        product.available = available
        product.category = category
        product.save()

        return HttpResponse(status=204)
    
    def delete(request,id):
        product = Product.objects.filter(id=id).first()
        product.delete()
        return render(request, "product.html")

    
class Renderizer(View):
    def index_product_template(request):
        return render(request, "product.html")
    
    def index_plantilla(request):
        return render(request, "plantilla.html")
    
    def index_pagina_diplomado(request):
        return render(request, "pagina_diplomado.html")

    def index_maqui_page(request):
        return render(request, "maqui_page.html")

    def index_golosina_page(request):
        return render(request, "golosina_page.html")

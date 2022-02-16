from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
#IMPORT MODELOS
from app.erp.models import *

#vista basadas en funciones
def myFirstView(request):
    data = {
        "first_name":"Andres",
        "lastname":"Quintero",
        "age":33,
        "msg":"mi primera vista"
    }
    return JsonResponse(data)

#enviar a un html para que renderice
def mySecondView(request):
    data = {
        "first_name":"Andres",
        "lastname":"Quintero",
        "age":33,
        "msg":"mi primera vista"
    }
    return render(request,'index.html',data)

def mySecondView(request):
    data = {
        "first_name":"Andres",
        "lastname":"Quintero",
        "age":33,
        "msg":"mi primera vista"
    }
    return render(request,'index.html',data)

def myFirstModel(request):
    data = {
        "name":"Categorias",
        "categorias":Category.objects.all()

    }
    return render(request,'index.html',data)

def myFirstProductos(request):
    data = {
        "name":"Productos",
        "productos":Product.objects.all()

    }
    return render(request,'second.html',data)
#vista basada en clases
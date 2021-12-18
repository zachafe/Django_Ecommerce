from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

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
#vista basada en clases